"""Operaciones vectoriales sencillas para busqueda por similitud."""

import numpy as np
from numpy.typing import ArrayLike, NDArray


def cosine_similarity(query: ArrayLike, document_vectors: ArrayLike) -> NDArray[np.float64]:
    """Calcula similitud coseno de una consulta con cada fila documental."""
    query_vector = np.asarray(query, dtype=float)
    matrix = np.asarray(document_vectors, dtype=float)
    if query_vector.ndim != 1 or matrix.ndim != 2:
        raise ValueError("La consulta debe ser un vector y los documentos una matriz.")
    if matrix.shape[1] != query_vector.shape[0]:
        raise ValueError("La consulta y los documentos deben compartir dimensiones.")

    denominators = np.linalg.norm(matrix, axis=1) * np.linalg.norm(query_vector)
    numerators = matrix @ query_vector
    return np.divide(
        numerators,
        denominators,
        out=np.zeros_like(numerators, dtype=float),
        where=denominators != 0,
    )


def rank_by_cosine(
    query: ArrayLike, document_vectors: ArrayLike, top_k: int
) -> list[tuple[int, float]]:
    """Devuelve indices y similitudes en orden descendente estable."""
    if top_k < 1:
        raise ValueError("top_k debe ser al menos 1.")
    similarities = cosine_similarity(query, document_vectors)
    indices = np.argsort(-similarities, kind="stable")[:top_k]
    return [(int(index), float(similarities[index])) for index in indices]