# config.py
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# API Keys
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Pinecone index name
INDEX_NAME = os.getenv("PINECONE_INDEX", "medical-chatbot")

# Data folder (where your PDFs are stored)
DATA_PATH = os.getenv("DATA_PATH", "../data")


# Default session (used if not provided by app)
DEFAULT_SESSION_ID = os.getenv("DEFAULT_SESSION_ID", "user123")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 20))
RETRIEVER_K = int(os.getenv("RETRIEVER_K", 3))

