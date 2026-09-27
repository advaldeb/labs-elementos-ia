"""Pruebas de configuracion y seleccion de proveedor sin llamadas de red."""

import sys
from types import ModuleType

import pytest
from pydantic import ValidationError

from llm_engineering.models import ModelRegistry, get_llm, load_model_registry


class FakeChatModel:
    """Sustituto local de un adaptador LangChain para las pruebas."""

    def __init__(self, **kwargs: object) -> None:
        self.kwargs = kwargs


@pytest.mark.parametrize(
    ("provider", "package_name", "class_name"),
    [
        ("ollama", "langchain_ollama", "ChatOllama"),
        ("openai", "langchain_openai", "ChatOpenAI"),
        ("anthropic", "langchain_anthropic", "ChatAnthropic"),
    ],
)
def test_get_llm_selects_configured_adapter(
    monkeypatch: pytest.MonkeyPatch,
    provider: str,
    package_name: str,
    class_name: str,
) -> None:
    """Cada proveedor selecciona su adaptador sin invocar un servicio externo."""
    provider_module = ModuleType(package_name)
    setattr(provider_module, class_name, FakeChatModel)
    monkeypatch.setitem(sys.modules, package_name, provider_module)

    model = get_llm(provider, model="modelo-de-prueba", temperature=0.4)

    assert isinstance(model, FakeChatModel)
    assert model.kwargs["model"] == "modelo-de-prueba"
    assert model.kwargs["temperature"] == 0.4


def test_model_registry_rejects_unknown_provider() -> None:
    """El esquema Pydantic limita el registro a proveedores soportados."""
    with pytest.raises(ValidationError):
        ModelRegistry.model_validate({"providers": {"desconocido": {"model": "x"}}})


def test_load_model_registry_includes_three_providers() -> None:
    """La configuracion inicial declara los tres adaptadores del curso."""
    registry = load_model_registry()

    assert set(registry.providers) == {"ollama", "openai", "anthropic"}