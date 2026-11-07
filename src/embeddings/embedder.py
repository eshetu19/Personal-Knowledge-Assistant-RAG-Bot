import numpy as np
from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

EMBEDDING_MODEL = "gemini-embedding-001"


def _embed_texts(texts: list[str], task_type: str) -> np.ndarray:
    if not isinstance(texts, list):
        raise TypeError("texts must be a list of strings")
    if not texts:
        raise ValueError("cannot embed an empty list")
    for text in texts:
        if not isinstance(text, str):
            raise TypeError("Every item must be string")
        if not text.strip():
            raise ValueError("Text inputs cannot be empty")
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=texts,
        config=types.EmbedContentConfig(
            task_type=task_type
        )
    )
    if not response.embeddings:
        raise RuntimeError("Gemini returned no embeddings")
    if len(response.embeddings) != len(texts):
        raise RuntimeError(
            "The number of returned embeddings doesnot match the number of inputs")
    embeddings = np.asarray(
        [item.values for item in response.embeddings],
        dtype=np.float32
    )
    if embeddings.ndim != 2:
        raise RuntimeError("Unexpected embedding dimensions.")
    if not np.isfinite(embeddings).all():
        raise RuntimeError("Embedding contains invalid numbers.")
    return embeddings


def embed_document_chunks(chunks: list[str]) -> np.ndarray:
    return _embed_texts(
        texts=chunks,
        task_type="RETRIEVAL_DOCUMENT"
    )


def embed_query(query: str) -> np.ndarray:
    if not isinstance(query, str):
        raise TypeError("Query must be a string.")
    if not query.strip():
        raise ValueError("Query cannot be empty")
    embeddings = _embed_texts(
        texts=[query],
        task_type="RETRIEVAL_QUERY"
    )
    return embeddings[0]
