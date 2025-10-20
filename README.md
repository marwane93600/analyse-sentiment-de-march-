
# Analyse de sentiment des articles économiques (FR)

Projet Python simple et propre pour **récupérer des actualités économiques** (NewsAPI), **analyser le sentiment** (TextBlob) et **visualiser la répartition** (Matplotlib).  
Conçu pour un **portfolio étudiant CMI D3S (Big Data)** – lisible, exécutable et prêt à être montré sur un CV/LinkedIn.

## 🚀 Aperçu du pipeline
1. Récupération des articles (FR) avec NewsAPI (`everything`, tri par date)
2. Prétraitement (fusion titre + description)
3. Analyse de sentiment (polarity ∈ [-1, 1] + label Positif/Neutre/Négatif)
4. Export CSV + graphique PNG de la répartition

## 📦 Installation
```bash
# Python 3.10+ recommandé
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Configuration
Copiez `.env.example` vers `.env` et renseignez votre clé NewsAPI :
```env
NEWS_API_KEY=VOTRE_CLE_API_ICI
```
> Obtenez une clé gratuite sur https://newsapi.org/

## ▶️ Exécution
```bash
python app.py
```
Sorties générées :
- `articles_sentiment.csv`
- `sentiment_graphique.png`

## ✅ Tests (facultatif)
```bash
pip install -r requirements.txt
pytest -q
```

## 📂 Structure
```text
analyse-sentiment-de-march-/
├── app.py
├── sentiment_utils.py
├── tests/
│   └── test_sentiment.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🧰 Tech
- Python, requests, pandas, matplotlib
- TextBlob + NLTK (polarity)
- Dotenv (gestion des secrets)

---
© 2025 – Marwane El Bachir · CMI D3S – Université Paris Nanterre
