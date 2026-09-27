"""Contratos validados para la configuracion de modelos y del entorno."""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

ProviderName = Literal["ollama", "openai", "anthropic"]


class ProviderConfig(BaseModel):
    """Configuracion de un proveedor y su identificador de modelo."""

    model_config = ConfigDict(extra="forbid")

    model: str = Field(min_length=1)
    base_url: str | None = None

    @field_validator("model")
    @classmethod
    def model_must_not_be_blank(cls, value: str) -> str:
        """Rechaza nombres vacios o compuestos solo por espacios."""
        cleaned_value = value.strip()
        if not cleaned_value:
            raise ValueError("El nombre del modelo no puede estar vacio.")
        return cleaned_value


class ModelRegistry(BaseModel):
    """Registro de modelos que se carga desde `config/models.yaml`."""

    model_config = ConfigDict(extra="forbid")

    providers: dict[ProviderName, ProviderConfig]


class RuntimeSettings(BaseModel):
    """Parametros generales de ejecucion de los laboratorios."""

    model_config = ConfigDict(extra="forbid")

    temperature: float = Field(default=0.0, ge=0.0, le=2.0)