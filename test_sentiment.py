
import math
from sentiment_utils import get_sentiment_label, get_polarity

def test_labels_fr():
    assert get_sentiment_label(get_polarity("Je suis très heureux aujourd'hui")) == "Positif"
    assert get_sentiment_label(get_polarity("C'est une catastrophe totale")) == "Négatif"
    # Phrase neutre simple
    assert get_sentiment_label(get_polarity("Ceci est une phrase.")) == "Neutre"
