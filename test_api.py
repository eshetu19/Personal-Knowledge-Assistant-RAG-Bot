
from google import genai
from src.config import GEMINI_API_KEY, CHAT_MODEL

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model = "gemini-3.5-flash-lite",
    contents="Explain RAG in two sentences."
)

print(response.text)
