from langchain_huggingface import HuggingFaceEmbeddings




def get_embeddings(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """Return a HuggingFaceEmbeddings instance."""
    return HuggingFaceEmbeddings(model_name=model_name)