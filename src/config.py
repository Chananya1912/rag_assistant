import os
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

EMBEDDING_MODEL = "mistral-embed"
LLM_MODEL = "codestral-2508"

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "fashion_documents"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50