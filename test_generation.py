from src.generation.generator import generate_answer


question = "What was my plan for improving my software engineering skills?"


retrieved_chunks = [
    {
        "chunk": {
            "chunk_id": 0,
            "text": "I should practice Python programming every day.",
            "source": "learning-notes.txt"
        },
        "score": 0.94
    },
    {
        "chunk": {
            "chunk_id": 1,
            "text": "I need to build and ship real-world projects.",
            "source": "career-notes.txt"
        },
        "score": 0.89
    },
    {
        "chunk": {
            "chunk_id": 2,
            "text": "I want to become a professional software engineer.",
            "source": "career-notes.txt"
        },
        "score": 0.82
    }
]


answer = generate_answer(
    question=question,
    retrieved_chunks=retrieved_chunks
)


print("\nPERSONAL KNOWLEDGE ASSISTANT")
print("-" * 40)
print("Question:", question)
print("\nAnswer:")
print(answer)
