"""Carga configuracion y construye modelos de chat sin acoplar al proveedor."""

from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml

from genai.models.config import ModelRegistry, ProviderName, RuntimeSettings

if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel

_COURSE_ROOT = Path(__file__).resolve().parents[3]
_SUPPORTED_PROVIDERS: dict[str, ProviderName] = {
    "ollama": "ollama",
    "openai": "openai",
    "anthropic": "anthropic",
}


def load_model_registry(config_path: str | Path | None = None) -> ModelRegistry:
    """Lee y valida el registro YAML de modelos."""
    path = Path(config_path) if config_path else _COURSE_ROOT / "config" / "models.yaml"
    with path.open(encoding="utf-8") as config_file:
        raw_config = yaml.safe_load(config_file) or {}
    return ModelRegistry.model_validate(raw_config)


def load_runtime_settings(config_path: str | Path | None = None) -> RuntimeSettings:
    """Lee y valida los parametros generales del curso."""
    path = Path(config_path) if config_path else _COURSE_ROOT / "config" / "settings.yaml"
    with path.open(encoding="utf-8") as config_file:
        raw_config = yaml.safe_load(config_file) or {}
    return RuntimeSettings.model_validate(raw_config)


def get_llm(
    provider: ProviderName | str,
    model: str | None = None,
    temperature: float | None = None,
    *,
    config_path: str | Path | None = None,
    **kwargs: Any,
) -> BaseChatModel:
    """Construye un modelo LangChain para Ollama, OpenAI o Anthropic.

    El argumento `model` tiene prioridad sobre la variable de entorno y YAML.
    Las claves nunca se reciben como argumento: cada SDK las lee del entorno.
    """
    normalized_provider = provider.strip().lower()
    if normalized_provider not in _SUPPORTED_PROVIDERS:
        raise ValueError(
            f"Proveedor no compatible: {provider!r}. "
            "Usa 'ollama', 'openai' o 'anthropic'."
        )

    provider_name = _SUPPORTED_PROVIDERS[normalized_provider]
    registry = load_model_registry(config_path)
    if provider_name not in registry.providers:
        raise ValueError(f"No hay configuracion para el proveedor {provider_name!r}.")

    provider_config = registry.providers[provider_name]
    model_name = (
        model
        or os.getenv(f"{provider_name.upper()}_MODEL")
        or provider_config.model
    ).strip()
    if not model_name:
        raise ValueError("El nombre del modelo no puede estar vacio.")

    selected_temperature = (
        temperature
        if temperature is not None
        else load_runtime_settings().temperature
    )
    if not 0.0 <= selected_temperature <= 2.0:
        raise ValueError("temperature debe estar entre 0.0 y 2.0.")

    model_options = {"model": model_name, "temperature": selected_temperature, **kwargs}
    try:
        if provider_name == "ollama":
            from langchain_ollama import ChatOllama

            if base_url := os.getenv("OLLAMA_BASE_URL", provider_config.base_url):
                model_options["base_url"] = base_url
            return ChatOllama(**model_options)
        if provider_name == "openai":
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(**model_options)

        from langchain_anthropic import ChatAnthropic

        return ChatAnthropic(**model_options)
    except ImportError as error:
        package_name = {
            "ollama": "langchain-ollama",
            "openai": "langchain-openai",
            "anthropic": "langchain-anthropic",
        }[provider_name]
        raise ImportError(
            f"Instala {package_name} para usar el proveedor {provider_name!r}."
        ) from error