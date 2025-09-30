from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List




def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """Return documents keeping only `source` metadata and the page_content."""
    return [
    Document(page_content=doc.page_content, metadata={"source": doc.metadata.get("source")})
        for doc in docs
        ]




def split_documents(minimal_docs: List[Document], chunk_size: int = 500, chunk_overlap: int = 20) -> List[Document]:
    """Split documents into chunks using RecursiveCharacterTextSplitter."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(minimal_docs)