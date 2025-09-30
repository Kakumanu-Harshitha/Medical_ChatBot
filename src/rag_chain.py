# rag_chain.py
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq


def build_rag_chain(retriever, groq_api_key: str, model_name: str = "gemma2-9b-it"):
    """
    Build and return a RAG chain:
      - Retrieves top docs for the input
      - Formats them into the system prompt
      - Calls the Groq LLM
      - Returns a parsed string
    """
    # Initialize Groq LLM
    llm = ChatGroq(model_name=model_name, api_key=groq_api_key, temperature=0)

    # System prompt
    system_prompt = (
        "You are a Medical assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer the question. "
        "If you don't know the answer, say that you don't know. "
        "Use three sentences maximum and keep the answer concise.\n\n{context}"
    )

    # Chat prompt with memory placeholder
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    # Helper to format retrieved docs
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Build the RAG chain
    rag_chain = (
        RunnablePassthrough.assign(
            context=lambda x: format_docs(retriever.get_relevant_documents(x["input"]))
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
