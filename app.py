from flask import Flask, render_template, request, jsonify
from src.chatbot import create_chatbot_pipeline
from src.config import DEFAULT_SESSION_ID
import os

app = Flask(__name__)

# Initialize chatbot pipeline once
chatbot, retriever = create_chatbot_pipeline()

# Session memory (simple dictionary for demonstration)
chat_sessions = {}

# Homepage
@app.route("/")
def index():
    return render_template("chat.html")  # Make sure chat.html exists in templates folder

# Chat endpoint
@app.route("/get", methods=["POST"])
def chat():
    user_input = request.form.get("msg")
    session_id = request.form.get("session_id", DEFAULT_SESSION_ID)

    # Initialize session history if not present
    if session_id not in chat_sessions:
        chat_sessions[session_id] = []

    # Prepare config for session-based memory
    config = {"configurable": {"session_id": session_id}}

    # Invoke chatbot pipeline
    response = chatbot.invoke({"input": user_input}, config=config)

    # Extract string if response is a dict/object
    if isinstance(response, dict):
        # If your pipeline returns {'answer': '...'}
        answer_text = response.get("answer", str(response))
    else:
        answer_text = str(response)

    # Update session messages
    chat_sessions[session_id].append(("user", user_input))
    chat_sessions[session_id].append(("assistant", answer_text))

    # Return only the text to frontend
    return jsonify({"answer": answer_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
