
from textblob import TextBlob
import nltk

def ensure_nltk():
    """Télécharge les ressources nécessaires de NLTK si absentes."""
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")

def get_polarity(text: str) -> float:
    blob = TextBlob(text)
    return blob.sentiment.polarity

def get_sentiment_label(polarity: float) -> str:
    if polarity > 0:
        return "Positif"
    elif polarity < 0:
        return "Négatif"
    return "Neutre"
