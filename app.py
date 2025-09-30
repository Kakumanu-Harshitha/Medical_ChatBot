import streamlit as st
from src.chatbot import create_chatbot_pipeline
from src.config import DEFAULT_SESSION_ID


st.set_page_config(page_title="Medical QA Chatbot", layout="centered")


st.title("Medical QA — Retrieval-augmented Chatbot")
st.markdown("Ask medical questions. Answers are concise .")


# Initialize pipeline once (takes time on first run)
with st.spinner("Loading (this may take a while)..."):
    chatbot, retriever = create_chatbot_pipeline()


# session state for history
if "session_id" not in st.session_state:
    st.session_state.session_id = DEFAULT_SESSION_ID
if "messages" not in st.session_state:
    st.session_state.messages = []


# Input area
user_input = st.text_input("Your question:")
if st.button("Ask") and user_input:
    config = {"configurable": {"session_id": st.session_state.session_id}}
    with st.spinner("Generating answer..."):
        answer = chatbot.invoke({"input": user_input}, config=config)
    st.session_state.messages.append(("user", user_input))
    st.session_state.messages.append(("assistant", answer))


# Show conversation
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**Bot:** {msg}")