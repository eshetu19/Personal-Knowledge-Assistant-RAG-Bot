import numpy as np
from pathlib import Path

from src.vector_store.store import (load_vector_store, DEFAULT_STORAGE_DIR)


def retrieve_chunks(query_embedding: np.ndarray, top_k: int = 3, storage_dir: Path | str = DEFAULT_STORAGE_DIR) -> list[dict]:
    if not isinstance(top_k, int) or isinstance(top_k, bool):
        raise TypeError("top_k musst be integer.")
    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")
    query_embedding = np.asarray(query_embedding, dtype=np.float32)
    if query_embedding.ndim != 1:
        raise ValueError("Query embedding must be one dimensional")
    if not np.isfinite(query_embedding).all():
        raise ValueError("Query embedding contains invalid numbers.")
    chunks, document_embeddings = load_vector_store(storage_dir)

    if query_embedding.shape[0] != document_embeddings.shape[1]:
        raise ValueError(
            "Query and document embedding dimensions do not much.")
    query_magnitude = np.linalg.norm(query_embedding)
    document_magnitudes = np.linalg.norm(document_embeddings, axis=1)
    if query_magnitude == 0:
        raise ValueError("query embedding cannot be a zero vector.")
    if np.any(document_magnitudes == 0):
        raise ValueError("Stored embeddings  contain zero vectors")
    dot_products = np.dot(document_embeddings, query_embedding)

    scores = dot_products/(document_magnitudes*query_magnitude)

    ranked_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for index in ranked_indices:
        results.append({
            "chunk": chunks[int(index)],
            "score": float(scores[index])
        })
    return results
