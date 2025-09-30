from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from typing import List
from langchain.schema import Document




def load_pdf_files(data_path: str) -> List[Document]:
    """Load PDF files from a directory and return list of LangChain Documents."""
    loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents