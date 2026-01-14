import pickle

url_model = pickle.load(open("models/url_model.pkl", "rb"))
url_vectorizer = pickle.load(open("models/url_vectorizer.pkl", "rb"))

def url_ml_predict(url: str) -> int:
    vec = url_vectorizer.transform([url])
    return int(url_model.predict(vec)[0])
