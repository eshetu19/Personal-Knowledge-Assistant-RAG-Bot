import numpy as np


def rank_documents(query_vector: np.ndarray, document_vectors: np.ndarray, top_k: int = 3) -> list[dict]:
    if not isinstance(top_k, int) or isinstance(top_k, bool):
        raise TypeError("top_k musst be integer.")
    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")
    query_vector = np.asarray(query_vector, dtype=np.float32)
    document_vectors = np.asarray(document_vectors, dtype=np.float32)
    if query_vector.ndim != 1:
        raise ValueError("Query vector must be one dimensional")
    if document_vectors.ndim != 2:
        raise ValueError("Document vectors must be a 2 dimensional array.")
    if document_vectors.shape[0] == 0:
        raise ValueError("No document vectors provided.")
    if query_vector.shape[0] != document_vectors.shape[1]:
        raise ValueError("Query and document vector dimensions do not much.")
    if not np.isfinite(query_vector).all():
        raise ValueError("Query vector contains invalid numbers.")
    if not np.isfinite(document_vectors).all():
        raise ValueError("Document vector contains invalid numbers")
    query_magnitude = np.linalg.norm(query_vector)
    document_magnitueds = np.linalg.norm(document_vectors, axis=1)
    if query_magnitude == 0:
        raise ValueError("query vector cannot be a zero vector.")
    if np.any(document_magnitueds == 0):
        raise ValueError("Document vectors cannot contain zero vectors")
    dot_products = np.dot(document_vectors, query_vector)
    scores = dot_products/(document_magnitueds*query_magnitude)

    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for index in top_indices:
        results.append(
            {
                "index": int(index),
                "score": float(scores[index])
            }
        )
    return results
