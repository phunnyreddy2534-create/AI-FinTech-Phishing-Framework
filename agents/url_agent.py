import pickle
from pathlib import Path

MODEL_PATH = Path("models")

with open(MODEL_PATH / "url_model.pkl", "rb") as f:
    url_model = pickle.load(f)

with open(MODEL_PATH / "url_vectorizer.pkl", "rb") as f:
    url_vectorizer = pickle.load(f)

def analyze_url(url: str) -> str:
    vector = url_vectorizer.transform([url])
    prediction = url_model.predict(vector)[0]
    return "PHISHING" if prediction == 1 else "SAFE"
