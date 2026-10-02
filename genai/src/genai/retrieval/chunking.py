"""Fragmentacion de texto basada en palabras para laboratorios."""


def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:
    """Divide texto en ventanas de palabras con solapamiento opcional."""
    if chunk_size < 1:
        raise ValueError("chunk_size debe ser al menos 1.")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap debe estar entre 0 y chunk_size - 1.")

    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        chunks.append(" ".join(words[start : start + chunk_size]))
        if start + chunk_size >= len(words):
            break
        start += chunk_size - overlap
    return chunks