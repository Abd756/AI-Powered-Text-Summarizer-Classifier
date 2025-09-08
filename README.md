
# AI-Powered Text Summarizer, Classifier & Chatbot

## Project Structure

- `modules/` : Python modules for each functionality
     - `summarization.py` : Abstractive text summarization using LLM
     - `classification.py` : Text classification logic (with support for 'Irrelevant' detection)
     - `assistant.py` : Handles user queries, combines summarization and classification
     - `train_classifier.py` : Script to train/update the classifier
- `chatbot.py` : Command-line chatbot interface
- `streamlit_chatbot.py` : Modern web UI for chat (Streamlit)
- `requirements.txt` : List of required Python packages
- `README.md` : Project documentation

## Getting Started
1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2. Train the classifier (recommended after updating training data):
    ```
    python modules/train_classifier.py
    ```
3. Run the chatbot:
    - Command-line: `python chatbot.py`
    - Web UI: `streamlit run streamlit_chatbot.py`

## Features
- Summarizes user input using a powerful LLM (LangChain + OpenAI)
- Classifies input into categories: Product Info, Service Info, Other, Irrelevant
- Returns concise summaries and predicted categories
- Handles irrelevant queries gracefully
- Attractive chat UI (Streamlit) with modern design

## Example Workflow
1. User enters a message (question, description, etc.)
2. Assistant summarizes the input and predicts its category
3. Response includes both summary and category, or "No relevant information available" for irrelevant queries

---

This project uses LangChain, scikit-learn, and Streamlit for AI-powered text processing and chat.
