# Assistant Query Handling Module
# Functions for handling user queries and returning relevant summaries and categories

from modules.summarization import summarize_documents
from modules.classification import classify_text

CATEGORIES = ["Product Info", "Service Info", "Other"]

def assistant_response(text: str) -> str:
    """
    Takes input text, summarizes it using LLM (abstractive), classifies it, and returns a clean response.
    """
    # Summarize using LLM (abstractive)
    summary = summarize_documents([text])[0]
    # Classify
    category = classify_text(summary, CATEGORIES)
    # Respond
    if category:
        return f"Summary: {summary}\nCategory: {category}"
    else:
        return "No relevant information available."

# Example usage:
# response = assistant_response("Your input text here.")
# print(response)

