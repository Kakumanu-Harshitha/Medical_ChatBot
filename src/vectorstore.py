from langchain_pinecone import PineconeVectorStore
from langchain.schema import Document
from typing import List
def init_vector_store(text_chunks: List[Document], embeddings, index_name: str):
    """Create (or reuse) a Pinecone index and return a connected VectorStore."""
    PineconeVectorStore.from_documents(text_chunks, embeddings, index_name=index_name)
    vector_store = PineconeVectorStore.from_existing_index(index_name, embeddings)
    return vector_store

def get_retriever(vector_store, k: int = 3):
    return vector_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
