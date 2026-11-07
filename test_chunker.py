from src.processing.chunker import chunk_text


sample_text = """
Social Extract is an application that helps people
intentionally consume social media content.

The first feature is a distraction-free feed.
Users only see content they intentionally selected.

The second feature is smart time limits.
Users can establish daily limits for different platforms.

The third feature is personal playlists.
Users can organize useful videos and posts into collections.
"""

try:
    chunks = chunk_text(
        sample_text,
        chunk_size=150,
        chunk_overlap=30
    )

    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks):
        print(f"\nCHUNK {index + 1}")
        print("-" * 40)
        print(chunk)
        print(f"Characters: {len(chunk)}")

except (TypeError, ValueError) as error:
    print("Chunking error:", error)







# import numpy as np

# from similarity import rank_documents

# query = np.array([0.8, 0.6])
# documents = np.array(
#     [[0.9, 0.4], [-0.5, 0.8], [0.7, 0.7], [0.1, 0.2], [0.8, 0.6]])
# results = rank_documents(
#     query_vector=query,
#     document_vectors=documents,
#     top_k=3
# )
# for result in results:
#     print(
#         f"Document index:{result['index']}",
#         f"Similarity:{result['score']:.4f}"
#     )
