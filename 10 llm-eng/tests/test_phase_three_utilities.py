"""Pruebas de utilidades locales de evaluacion y recuperacion."""

import numpy as np
import pytest

from llm_engineering.evaluation.metrics import (
    classification_accuracy,
    exact_match_rate,
    hit_rate_at_k,
    mean_reciprocal_rank,
    precision_at_k,
    recall_at_k,
    schema_compliance_rate,
    semantic_similarity_score,
)
from llm_engineering.evaluation.costs import (
    ModelPricing,
    PricingCatalog,
    estimate_cost_usd,
    load_pricing_catalog,
)
from pydantic import ValidationError
from llm_engineering.retrieval.chunking import chunk_text
from llm_engineering.retrieval.vector_search import cosine_similarity, rank_by_cosine


def test_chunk_text_applies_overlap_without_losing_words() -> None:
    assert chunk_text("a b c d e", chunk_size=3, overlap=1) == ["a b c", "c d e"]


def test_chunk_text_rejects_invalid_window() -> None:
    with pytest.raises(ValueError):
        chunk_text("a b", chunk_size=2, overlap=2)


def test_cosine_ranking_returns_expected_document_first() -> None:
    vectors = np.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])

    assert cosine_similarity([1.0, 0.0], vectors).tolist() == [1.0, 0.0, 0.0]
    assert rank_by_cosine([1.0, 0.0], vectors, top_k=2) == [(0, 1.0), (1, 0.0)]


def test_ranking_metrics_match_known_relevance() -> None:
    ranking = ["d3", "d1", "d2"]
    relevant = {"d1", "d2"}

    assert hit_rate_at_k(ranking, relevant, 2) == 1.0
    assert precision_at_k(ranking, relevant, 2) == 0.5
    assert recall_at_k(ranking, relevant, 2) == 0.5
    assert mean_reciprocal_rank([ranking], [relevant]) == 0.5


def test_basic_evaluation_metrics() -> None:
    assert exact_match_rate(["si", "no"], ["si", "sí"]) == 0.5
    assert classification_accuracy(["a", "b"], ["a", "c"]) == 0.5
    assert schema_compliance_rate([True, False, True]) == pytest.approx(2 / 3)


def test_semantic_similarity_uses_paired_embedding_cosine() -> None:
    predictions = np.array([[1.0, 0.0], [1.0, 1.0]])
    references = np.array([[1.0, 0.0], [0.0, 1.0]])

    assert semantic_similarity_score(predictions, references) == pytest.approx(
        (1.0 + 2**-0.5) / 2
    )


def test_semantic_similarity_rejects_unaligned_embeddings() -> None:
    with pytest.raises(ValueError, match="dimensiones alineadas"):
        semantic_similarity_score([[1.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]])


def test_cost_estimation_uses_configured_rates_only() -> None:
    catalog = PricingCatalog(models={
        "local/mock": ModelPricing(
            input_usd_per_million_tokens=2.0,
            output_usd_per_million_tokens=4.0,
            source="tarifa de prueba",
            effective_date="2026-09-27",
        ),
        "unknown/rates": ModelPricing(),
    })

    assert estimate_cost_usd("local", "mock", 1000, 500, catalog=catalog) == pytest.approx(0.004)
    assert estimate_cost_usd("unknown", "rates", 1000, 500, catalog=catalog) is None
    assert estimate_cost_usd("local", "mock", None, 500, catalog=catalog) is None


def test_pricing_requires_complete_rates_and_provenance() -> None:
    with pytest.raises(ValidationError, match="ambas tarifas"):
        ModelPricing(input_usd_per_million_tokens=1.0)
    with pytest.raises(ValidationError, match="source y effective_date"):
        ModelPricing(
            input_usd_per_million_tokens=1.0,
            output_usd_per_million_tokens=2.0,
        )


def test_course_pricing_catalog_keeps_unverified_costs_unknown() -> None:
    catalog = load_pricing_catalog()

    assert catalog.models
    assert all(
        pricing.input_usd_per_million_tokens is None
        and pricing.output_usd_per_million_tokens is None
        for pricing in catalog.models.values()
    )