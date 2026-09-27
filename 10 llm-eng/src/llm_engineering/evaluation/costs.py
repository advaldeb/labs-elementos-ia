"""Estimacion de costos con tarifas configurables y versionables."""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

_COURSE_ROOT = Path(__file__).resolve().parents[3]


class ModelPricing(BaseModel):
    """Tarifas USD por millon de tokens para un modelo configurable."""

    model_config = ConfigDict(extra="forbid")

    input_usd_per_million_tokens: float | None = Field(default=None, ge=0.0)
    output_usd_per_million_tokens: float | None = Field(default=None, ge=0.0)
    source: str | None = None
    effective_date: date | None = None

    @model_validator(mode="after")
    def rates_require_provenance(self) -> ModelPricing:
        """Exige tarifas completas y procedencia antes de estimar costo."""
        input_configured = self.input_usd_per_million_tokens is not None
        output_configured = self.output_usd_per_million_tokens is not None
        if input_configured != output_configured:
            raise ValueError("Configura ambas tarifas o deja ambas como null.")
        if input_configured and (not self.source or self.effective_date is None):
            raise ValueError("Las tarifas requieren source y effective_date.")
        return self


class PricingCatalog(BaseModel):
    """Catalogo de tarifas indexado por `provider/model`."""

    model_config = ConfigDict(extra="forbid")

    models: dict[str, ModelPricing]


def load_pricing_catalog(config_path: str | Path | None = None) -> PricingCatalog:
    """Carga tarifas desde YAML sin asumir precios actuales de proveedores."""
    path = Path(config_path) if config_path else _COURSE_ROOT / "config" / "pricing.yaml"
    with path.open(encoding="utf-8") as pricing_file:
        raw_pricing = yaml.safe_load(pricing_file) or {}
    return PricingCatalog.model_validate(raw_pricing)


def estimate_cost_usd(
    provider: str,
    model: str,
    input_tokens: int | None,
    output_tokens: int | None,
    *,
    catalog: PricingCatalog | None = None,
) -> float | None:
    """Estima costo solo si hay tokens y tarifas configuradas para el modelo."""
    if input_tokens is None or output_tokens is None:
        return None
    if input_tokens < 0 or output_tokens < 0:
        raise ValueError("Los conteos de tokens no pueden ser negativos.")

    pricing = (catalog or load_pricing_catalog()).models.get(f"{provider}/{model}")
    if pricing is None:
        return None
    input_rate = pricing.input_usd_per_million_tokens
    output_rate = pricing.output_usd_per_million_tokens
    if input_rate is None or output_rate is None:
        return None

    return (input_tokens * input_rate + output_tokens * output_rate) / 1_000_000