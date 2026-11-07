import json
import numpy as np
from pathlib import Path

from src import embeddings

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_STORAGE_DIR = PROJECT_ROOT/"storage"


def validate_data(chunks: list[dict], embeddings: np.ndarray) -> None:
    if not isinstance(chunks, list):
        raise TypeError("chunks must provided as list.")
    if not chunks:
        raise ValueError("cannot store an empty chunk collecton.")
    for index, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            raise TypeError(f"chunk at index:{index} must be a dictionary.")
        if not isinstance(chunk.get("text"), str):
            raise ValueError(
                f"chunk at index:{index},must contain text as string.")
        if not chunk["text"].strip():
            raise ValueError(f"chunk at index:{index} has empty text.")
    if embeddings.ndim != 2:
        raise ValueError("embeddings must be a two dimensional array.")
    if embeddings.shape[0] == 0 or embeddings.shape[1] == 0:
        raise ValueError("embeddings cannot have an empty dimension.")
    if len(chunks) != embeddings.shape[0]:
        raise ValueError("number of chunks must much number of embeddings.")
    if not np.isfinite(embeddings).all():
        raise ValueError("Embeddings contain Invalid numerical value")


def save_vector_store(
    chunks: list[dict],
    embeddings: np.ndarray,
    storage_dir: Path | str = DEFAULT_STORAGE_DIR
) -> None:
    """
    Save chunks and their embeddings to disk.
    """

    storage_path = Path(storage_dir)

    embeddings = np.asarray(embeddings, dtype=np.float32)

    # Validate the data before saving.
    validate_data(chunks, embeddings)

    # Create the storage directory if it doesn't exist.
    storage_path.mkdir(parents=True, exist_ok=True)

    embeddings_path = storage_path / "embeddings.npy"
    chunks_path = storage_path / "chunks.json"

    # Save embeddings.
    np.save(embeddings_path, embeddings)

    # Save chunks and metadata.
    with chunks_path.open("w", encoding="utf-8") as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Vector store saved successfully: {storage_path}")

def load_vector_store(storage_dir: Path | str = DEFAULT_STORAGE_DIR) -> tuple[list[dict], np.ndarray]:
    storage_path = Path(storage_dir)
    embeddings_path = storage_path/"embeddings.npy"
    chunks_path = storage_path/"chunks.json"
    if not embeddings_path.is_file():
        raise FileNotFoundError(
            f"embeddings file not found :{embeddings_path}")
    if not chunks_path.is_file():
        raise FileNotFoundError(f"chunks file not found:{chunks_path}")

    embeddings = np.load(embeddings_path, allow_pickle=False)

    with chunks_path.open("r", encoding="utf-8") as file:
        chunks = json.load(file)
    embeddings = np.asarray(embeddings, dtype=np.float32)
    validate_data(chunks, embeddings)
    return chunks, embeddings
