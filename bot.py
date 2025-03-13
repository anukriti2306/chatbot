import os
import streamlit as st
from groq import Groq
import time
import re  # Import regex module

# Set Streamlit page config
st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

# Load API Key from environment
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("🔑 Please set your GROQ_API_KEY environment variable!")
    st.stop()

# Initialize Groq API client
client = Groq(api_key=api_key)

# Streamlit UI Title
st.title("💬 Chat with AI")
st.caption("Powered by Groq API")

# Model selection dropdown
model_options = {
    "DeepSeek-R1-Distill-LLama-70B": "deepseek-r1-distill-llama-70b",
    "Llama 3.2 70B (8192)": "llama3-70b-8192",
}

selected_model = st.selectbox("🧠 Select Model:", list(model_options.keys()))

# Store selected model in session state
st.session_state.selected_model = model_options[selected_model]

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to clean up AI response (remove <think> tags)
def clean_response(text):
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
        st.write(msg["content"])  # Auto handles markdown

# User Input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Append user input to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user", avatar="🧑"):
        st.write(user_input)

    # Generate AI response with loading effect
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=st.session_state.selected_model,  # Dynamic model selection
                    messages=st.session_state.messages,
                    max_tokens=500,
                )
                ai_reply = response.choices[0].message.content
            except Exception as e:
                ai_reply = f"❌ Error: {e}"

        # Clean AI response to remove <think> tags
        ai_reply = clean_response(ai_reply)

        # Typing Effect Simulation with Proper Markdown
        response_container = st.empty()
        full_response = ""
        for char in ai_reply:
            full_response += char
            response_container.markdown(full_response + "▌")  # Typing effect
            time.sleep(0.01)  # Simulate typing delay

        response_container.markdown(full_response)  # Final output

    # Append AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
