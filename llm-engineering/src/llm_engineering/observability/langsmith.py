"""Integracion LangSmith optativa y desactivada sin configuracion explicita."""

from __future__ import annotations

import os
from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from pydantic import BaseModel, ConfigDict, Field

P = ParamSpec("P")
R = TypeVar("R")


class LangSmithSettings(BaseModel):
    """Configuracion segura para observabilidad remota opcional."""

    model_config = ConfigDict(extra="forbid")

    enabled: bool = False
    project_name: str = Field(default="llm-engineering-labs", min_length=1)
    api_key_configured: bool = False
    endpoint_configured: bool = False


def load_langsmith_settings(environ: Mapping[str, str] | None = None) -> LangSmithSettings:
    """Lee variables LangSmith sin devolver ni imprimir secretos."""
    environment = os.environ if environ is None else environ
    raw_enabled = environment.get("LANGSMITH_TRACING", "false").strip().casefold()
    if raw_enabled not in {"true", "false", "1", "0", "yes", "no", "on", "off"}:
        raise ValueError("LANGSMITH_TRACING debe ser un valor booleano reconocible.")

    enabled = raw_enabled in {"true", "1", "yes", "on"}
    project_name = environment.get("LANGSMITH_PROJECT", "llm-engineering-labs").strip()
    if not project_name:
        raise ValueError("LANGSMITH_PROJECT no puede estar vacio.")

    return LangSmithSettings(
        enabled=enabled,
        project_name=project_name,
        api_key_configured=bool(environment.get("LANGSMITH_API_KEY")),
        endpoint_configured=bool(environment.get("LANGSMITH_ENDPOINT")),
    )


def _require_credentials(settings: LangSmithSettings) -> None:
    """Exige clave antes de activar cualquier envio de trazas."""
    if settings.enabled and not settings.api_key_configured:
        raise ValueError("LangSmith esta activado, pero LANGSMITH_API_KEY no esta configurada.")


@contextmanager
def langsmith_tracing(*, enabled: bool | None = None) -> Iterator[None]:
    """Activa contexto de trazas solo con consentimiento y clave configurada."""
    settings = load_langsmith_settings()
    tracing_enabled = settings.enabled if enabled is None else enabled
    if tracing_enabled:
        _require_credentials(settings.model_copy(update={"enabled": True}))

    from langsmith import tracing_context

    with tracing_context(enabled=tracing_enabled, project_name=settings.project_name):
        yield


def traceable_if_enabled(
    *, name: str | None = None
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Decora una funcion con LangSmith solo si el entorno lo habilita."""
    def decorate(function: Callable[P, R]) -> Callable[P, R]:
        settings = load_langsmith_settings()
        if not settings.enabled:
            return function
        _require_credentials(settings)

        from langsmith import traceable

        traced = traceable(
            name=name or function.__name__,
            project_name=settings.project_name,
        )(function)

        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return traced(*args, **kwargs)

        return wrapper

    return decorate