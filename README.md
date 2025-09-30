# Medical RAG Chatbot with Groq and Pinecone
This project is a sophisticated, conversational medical chatbot that leverages a Retrieval-Augmented Generation (RAG) architecture to answer questions based on a provided medical text. It uses state-of-the-art, high-speed language models from Groq and a persistent vector store from Pinecone to deliver fast, accurate, and context-aware responses.

# Features

**High-Speed Responses:**
 Powered by the Groq API, utilizing powerful models like Gemma 2 for near-instantaneous answers.

**Document-Grounded Answers:**
The chatbot's knowledge is based on a specific medical document (Medical_book.pdf), ensuring that its responses are accurate and relevant to the provided context.

**Conversational Memory:**
 Remembers the history of the conversation, allowing for follow-up questions and more natural interactions.

**Scalable Vector Storage:**
 Uses Pinecone to store document embeddings, allowing for efficient retrieval from a large corpus of text.

**Modern LangChain Architecture:**
Built using the latest LangChain Expression Language (LCEL) and RunnableWithMessageHistory for a clean, maintainable, and scalable codebase.

# How It Works (RAG Architecture)

**Data Ingestion:**
A large medical PDF is loaded, split into smaller, manageable chunks of text.

**Embedding:**
 Each text chunk is converted into a numerical vector representation (an embedding) using a sentence-transformer model.

**Indexing:**
 These embeddings are stored and indexed in a Pinecone vector database for fast similarity searching.

**Retrieval:**
When a user asks a question, the chatbot embeds the query and retrieves the most relevant text chunks from Pinecone.

**Generation:**
 The original question, the retrieved context, and the conversation history are passed to the Groq LLM, which generates a final, coherent answer.