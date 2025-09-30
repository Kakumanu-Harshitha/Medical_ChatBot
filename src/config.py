from dotenv import load_dotenv
import os
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
INDEX_NAME = os.getenv("PINECONE_INDEX", "medical-chatbot")
DATA_PATH = os.getenv("DATA_PATH", "../data")
DEFAULT_SESSION_ID = os.getenv("DEFAULT_SESSION_ID", "user123")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 20))
RETRIEVER_K = int(os.getenv("RETRIEVER_K", 3))

