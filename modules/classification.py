# Classification Module
# Functions for training and applying text classification models

from typing import List, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

MODEL_PATH = "classifier_model.pkl"
VECTORIZER_PATH = "classifier_vectorizer.pkl"

# Train classifier (run once, or retrain as needed)
def train_classifier(texts: List[str], labels: List[str]) -> None:
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, labels)
    # Save model and vectorizer
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(clf, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

# Predict category for a single text
def classify_text(text: str, categories: List[str]) -> Optional[str]:
    # Load model and vectorizer
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        return None
    with open(MODEL_PATH, "rb") as f:
        clf = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    X = vectorizer.transform([text])
    pred = clf.predict(X)[0]
    # Only return if prediction is in categories
    if pred in categories:
        return pred
    return None

# Example usage (run once to train):
# texts = ["SmartWidget automates tasks", "Support team available", "Company history"]
# labels = ["Product Info", "Service Info", "Other"]
# train_classifier(texts, labels)