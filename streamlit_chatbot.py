import streamlit as st
from modules.assistant import assistant_response

st.set_page_config(page_title="AI-Powered Chatbot", page_icon="🤖", layout="centered")
st.markdown("""
<style>
body {
    background-color: #181818;
}
.stChatMessage {
    border-radius: 18px;
    padding: 16px 20px;
    margin-bottom: 16px;
    max-width: 80%;
    font-size: 1.1em;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.user {
    background: linear-gradient(90deg, #43e97b 0%, #38f9d7 100%);
    color: #181818;
    margin-left: auto;
    text-align: right;
}
.assistant {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: #fff;
    margin-right: auto;
    text-align: left;
}
.stTitle {
    color: #fff;
}
.stTextInput > div > input {
    background-color: #222;
    color: #fff;
    border-radius: 8px;
    border: 1px solid #444;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI-Powered Chatbot")
st.write("Type your message below and press Enter. Type 'exit' to end the chat.")

user_input = st.text_input("You:", "", key="user_input", placeholder="Ask me anything about SmartWidget, support, or services...")

if user_input and user_input.strip().lower() != "exit":
    response = assistant_response(user_input)
    st.markdown(f'<div class="stChatMessage user"><strong>You:</strong> {user_input}</div>', unsafe_allow_html=True)
    # Add new lines before 'Category:' for better separation
    formatted_message = response.replace('Summary:', '<span style="font-weight:bold; font-size:1.1em; color:#ffd700;">Summary:</span>')
    formatted_message = formatted_message.replace('Category:', '<br><br><span style="font-weight:bold; font-size:1.1em; color:#00e6e6;">Category:</span>')
    st.markdown(f'<div class="stChatMessage assistant"><strong>Assistant:</strong> {formatted_message}</div>', unsafe_allow_html=True)

if user_input.strip().lower() == "exit":
    st.write("Goodbye!")
