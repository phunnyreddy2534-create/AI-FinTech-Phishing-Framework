import pickle

sms_model = pickle.load(open("models/sms_model.pkl", "rb"))
sms_vectorizer = pickle.load(open("models/sms_vectorizer.pkl", "rb"))

def sms_ml_predict(text: str) -> int:
    vec = sms_vectorizer.transform([text])
    return int(sms_model.predict(vec)[0])
