import pickle
from pathlib import Path

MODEL_PATH = Path("models")

with open(MODEL_PATH / "sms_model.pkl", "rb") as f:
    sms_model = pickle.load(f)

with open(MODEL_PATH / "sms_vectorizer.pkl", "rb") as f:
    sms_vectorizer = pickle.load(f)

def analyze_sms(text: str) -> str:
    vector = sms_vectorizer.transform([text])
    prediction = sms_model.predict(vector)[0]
    return "SMISHING" if prediction == 1 else "SAFE"
