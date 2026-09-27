"""Metricas deterministas para evaluar respuestas y recuperacion."""

from collections.abc import Sequence, Set
from typing import TypeVar

import numpy as np
from numpy.typing import ArrayLike

Item = TypeVar("Item")


def _validate_k(k: int) -> None:
    """Comprueba que k sea positivo."""
    if k < 1:
        raise ValueError("k debe ser al menos 1.")


def _validate_pair_lengths(predictions: Sequence[object], references: Sequence[object]) -> None:
    """Comprueba que existan predicciones y referencias alineadas."""
    if not predictions:
        raise ValueError("La evaluacion requiere al menos un ejemplo.")
    if len(predictions) != len(references):
        raise ValueError("Predicciones y referencias deben tener la misma longitud.")


def exact_match_rate(predictions: Sequence[str], references: Sequence[str]) -> float:
    """Calcula la proporcion de cadenas exactamente iguales."""
    _validate_pair_lengths(predictions, references)
    return sum(prediction == reference for prediction, reference in zip(predictions, references)) / len(
        references
    )


def classification_accuracy(predictions: Sequence[Item], references: Sequence[Item]) -> float:
    """Calcula accuracy para etiquetas alineadas."""
    _validate_pair_lengths(predictions, references)
    return sum(prediction == reference for prediction, reference in zip(predictions, references)) / len(
        references
    )


def schema_compliance_rate(valid_records: Sequence[bool]) -> float:
    """Calcula la fraccion de registros que cumplen un esquema."""
    if not valid_records:
        raise ValueError("La evaluacion requiere al menos un registro.")
    return sum(valid_records) / len(valid_records)


def semantic_similarity_score(
    prediction_embeddings: ArrayLike,
    reference_embeddings: ArrayLike,
) -> float:
    """Calcula cosine similarity promedio entre pares de embeddings alineados.

    Los embeddings deben provenir del mismo modelo y ocupar el mismo espacio.
    Vectores nulos contribuyen cero; no se interpretan como equivalentes.
    """
    predictions = np.asarray(prediction_embeddings, dtype=float)
    references = np.asarray(reference_embeddings, dtype=float)
    if predictions.ndim != 2 or references.ndim != 2:
        raise ValueError("Los embeddings deben ser matrices bidimensionales.")
    if predictions.shape != references.shape:
        raise ValueError("Predicciones y referencias deben tener dimensiones alineadas.")
    if predictions.shape[0] == 0:
        raise ValueError("La evaluacion requiere al menos un par de embeddings.")

    numerators = np.sum(predictions * references, axis=1)
    denominators = np.linalg.norm(predictions, axis=1) * np.linalg.norm(references, axis=1)
    similarities = np.divide(
        numerators,
        denominators,
        out=np.zeros_like(numerators, dtype=float),
        where=denominators != 0,
    )
    return float(similarities.mean())


def hit_rate_at_k(retrieved: Sequence[Item], relevant: Set[Item], k: int) -> float:
    """Indica si aparece al menos un elemento relevante entre los primeros k."""
    _validate_k(k)
    return float(bool(set(retrieved[:k]) & relevant))


def precision_at_k(retrieved: Sequence[Item], relevant: Set[Item], k: int) -> float:
    """Calcula la proporcion de los primeros k resultados que son relevantes."""
    _validate_k(k)
    return len(set(retrieved[:k]) & relevant) / k


def recall_at_k(retrieved: Sequence[Item], relevant: Set[Item], k: int) -> float:
    """Calcula la proporcion de elementos relevantes recuperados entre los primeros k."""
    _validate_k(k)
    if not relevant:
        raise ValueError("Recall requiere al menos un elemento relevante.")
    return len(set(retrieved[:k]) & relevant) / len(relevant)


def reciprocal_rank(retrieved: Sequence[Item], relevant: Set[Item]) -> float:
    """Devuelve el reciproco del rango del primer resultado relevante, o cero."""
    for rank, item in enumerate(retrieved, start=1):
        if item in relevant:
            return 1 / rank
    return 0.0


def mean_reciprocal_rank(
    rankings: Sequence[Sequence[Item]], relevant_by_query: Sequence[Set[Item]]
) -> float:
    """Calcula MRR para rankings y conjuntos relevantes alineados por consulta."""
    _validate_pair_lengths(rankings, relevant_by_query)
    return sum(
        reciprocal_rank(ranking, relevant)
        for ranking, relevant in zip(rankings, relevant_by_query)
    ) / len(rankings)