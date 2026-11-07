import numpy as np
from pathlib import Path
from src import embeddings
from src.vector_store.store import (save_vector_store, load_vector_store)

chunks = [
    {
        "chunk_id": 0,
        "text": "I want to become professional software engineer.",
        "source": "career-notes.txt"
    },
    {
        "chunk_id": 1,
        "text": "I should practice python programming.",
        "source": "learning-notes.txt"
    },
    {
        "chunk_id": 2,
        "text": "my startup idea is nuzz.",
        "source": "startup-notes.txt"
    },

]

embeddings = np.array([
    [0.21, -0.45, 0.78],
    [0.31, -0.22, 0.65],
    [0.19, 0.82, 0.12]
], dtype=np.float32)

test_storage = Path("storage/test_vector_store")

save_vector_store(
    chunks=chunks,
    embeddings=embeddings,
    storage_dir=test_storage
)

loaded_chunks, loaded_embeddings = load_vector_store(storage_dir=test_storage)
print("\nloaded chunks:", len(loaded_chunks))
print("\nloaded_embeddings:", loaded_embeddings.shape)

print("\nchecking index alignment:")
for index in range(len(loaded_chunks)):
    print(f"\nindex:{index}")
    print("Text:", loaded_chunks[index]["text"])
    print("Embedding:", loaded_embeddings[index])

assert np.array_equal(embeddings, loaded_embeddings)

print("\nVector store test passed")
