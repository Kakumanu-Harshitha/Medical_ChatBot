import os
from langchain_core.runnables import RunnableWithMessageHistory
from .preprocessing import filter_to_minimal_docs, split_documents
from .embeddings import get_embeddings
from .vectorstore import init_vector_store, get_retriever
from .rag_chain import build_rag_chain
from .config import DATA_PATH, INDEX_NAME, CHUNK_SIZE, CHUNK_OVERLAP, RETRIEVER_K, GROQ_API_KEY
from .loaders import load_pdf_files
from langchain_community.chat_message_histories import ChatMessageHistory

def create_chatbot_pipeline(data_path: str = DATA_PATH, index_name: str = INDEX_NAME, session_history=None):
    """Create and return (chatbot_runnable, retriever) so callers can invoke."""
# 1. load
    raw_docs = load_pdf_files(data_path)


# 2. preprocess
    minimal_docs = filter_to_minimal_docs(raw_docs)
    text_chunks = split_documents(minimal_docs, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)


# 3. embeddings & vector store
    embeddings = get_embeddings()
    vector_store = init_vector_store(text_chunks, embeddings, index_name=index_name)


# 4. retriever
    retriever = get_retriever(vector_store, k=RETRIEVER_K)


# 5. rag chain
    rag_chain = build_rag_chain(retriever, groq_api_key=GROQ_API_KEY)


# 6. attach memory
    if session_history is None:
        session_history = ChatMessageHistory()


    chatbot = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id: session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    )


    return chatbot, retriever

if __name__ == "__main__":
    chatbot, retriever = create_chatbot_pipeline()
    print("✅ Chatbot ready. Type 'quit' to exit.")
    while True:
        user_query = input("Ask a medical question: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        if not user_query.strip():
            continue
    config = {"configurable": {"session_id": "user123"}}
    answer = chatbot.invoke({"input": user_query}, config=config)
    print("--- Answer ---")
    print("--------------")