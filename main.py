import argparse
from pathlib import Path

from src.ingestion.loader import load_text
from src.processing.cleaner import clean_text
from src.processing.chunker import chunk_text

from src.embeddings.embedder import (
    embed_document_chunks,
    embed_query
)

from src.vector_store.store import (
    save_vector_store,
    DEFAULT_STORAGE_DIR
)

from src.retrieval.retriever import retrieve_chunks
from src.generation.generator import generate_answer


PROJECT_ROOT = Path(__file__).resolve().parent
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


def ingest_documents():

    print("\nStarting document ingestion...")

    document_paths = list(DOCUMENTS_DIR.glob("*.txt"))

    if not document_paths:
        raise FileNotFoundError(
            f"No TXT documents found in {DOCUMENTS_DIR}"
        )

    all_chunks = []
    for document_path in document_paths:

        print(f"\nProcessing: {document_path.name}")

        
        raw_text = load_text(document_path)

        
        cleaned_text = clean_text(raw_text)

        
        text_chunks = chunk_text(
            cleaned_text,
            chunk_size=1000,
            chunk_overlap=150
        )
        for text in text_chunks:
            all_chunks.append({
                "chunk_id": len(all_chunks),
                "text": text,
                "source": document_path.name
            })

        print(f"Created {len(text_chunks)} chunks.")

    if not all_chunks:
        raise ValueError("No document chunks were generated.")

    print(f"\nTotal chunks: {len(all_chunks)}")

   
    chunk_texts = [
        chunk["text"] for chunk in all_chunks
    ]

    print("\nGenerating document embeddings...")

   
    embeddings = embed_document_chunks(chunk_texts)

    print("Document embeddings generated.")
    print("Embedding shape:", embeddings.shape)

    
    save_vector_store(
        chunks=all_chunks,
        embeddings=embeddings
    )

    print("\nDocument ingestion completed successfully!")


def ask_question(question: str) -> str:
    

    print("\nGenerating query embedding...")

    
    query_embedding = embed_query(question)

    print("Query embedding generated.")

    
    print("\nSearching your knowledge base...")

    retrieved_chunks = retrieve_chunks(
        query_embedding=query_embedding,
        top_k=3
    )

   
    print(f"\nRetrieved {len(retrieved_chunks)} chunks.")

    # for index, result in enumerate(retrieved_chunks, start=1):
    #     print(f"\nResult {index}")
    #     print("Score:", round(result["score"], 4))
    #     print("Source:", result["chunk"]["source"])
    #     print("Text:", result["chunk"]["text"])

    
    print("\nGenerating final answer...")

    answer = generate_answer(
        question=question,
        retrieved_chunks=retrieved_chunks
    )

    return answer


def main():
    parser = argparse.ArgumentParser(
        description="Personal Knowledge Assistant - RAG"
    )

    parser.add_argument(
        "--ingest",
        action="store_true",
        help="Process documents and build the knowledge base."
    )

    args = parser.parse_args()

    try:
        if args.ingest:
            ingest_documents()
            return
        embeddings_path = DEFAULT_STORAGE_DIR / "embeddings.npy"
        chunks_path = DEFAULT_STORAGE_DIR / "chunks.json"
        if not embeddings_path.exists() or not chunks_path.exists():
            print(
                "Knowledge base not found. "
                "Run: python main.py --ingest"
            )
            return
        print("\n================================")
        print(" PERSONAL KNOWLEDGE ASSISTANT")
        print("================================")
        print("Type 'exit' to quit.")
        while True:

            question = input("\nAsk Question: ").strip()

            if question.lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            if not question:
                print("Please enter a question.")
                continue

            answer = ask_question(question)

            print("\nAssistant:")
            print(answer)
    except (ValueError, TypeError, FileNotFoundError) as error:
        print(f"\nApplication error: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
