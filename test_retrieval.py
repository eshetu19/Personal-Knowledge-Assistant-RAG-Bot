import numpy as np
from src.retrieval.retriever import retrieve_chunks

query = np.array([0.31, -0.22, 0.65], dtype=np.float32)

results = retrieve_chunks(query_embedding=query, top_k=2,
                          storage_dir="storage/test_vector_store")

print("\nMost relevant notes:")

for rank, result in enumerate(results, start=1):
    print(f"\nRank:{rank}")
    print(f"Similarity:{result['score']:.4f}")
    print(f"Text:{result['chunk']['source']}")
    print(f"Source:{result['chunk']['source']}")
