
import os
import ssl
import sys
import requests
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from sentiment_utils import ensure_nltk, get_sentiment_label, get_polarity

# --- Entrée principale ---
def main():
    print("🚀 Lancement de l'analyse de sentiment...")

    # SSL : éviter certains environnements qui bloquent (optionnel)
    ssl._create_default_https_context = ssl._create_unverified_context

    # Chargement des variables d'environnement (.env)
    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print("❌ NEWS_API_KEY manquant. Renseignez-le dans un fichier .env (voir .env.example).")
        sys.exit(1)

    # Paramètres NewsAPI
    params = {
        "q": "économie OR economy",
        "language": "fr",
        "sortBy": "publishedAt",
        "pageSize": 100,
        "apiKey": api_key
    }
    url = "https://newsapi.org/v2/everything"

    print("🌐 Récupération des articles via NewsAPI...")
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur réseau/API: {e}")
        sys.exit(1)

    if data.get("status") != "ok" or "articles" not in data:
        print("❌ Réponse inattendue de l'API NewsAPI.")
        sys.exit(1)

    articles = data.get("articles", [])
    if not articles:
        print("🟡 Aucun article retourné par l'API.")
        sys.exit(0)

    print(f"✅ {len(articles)} articles récupérés. Nettoyage des données...")
    rows = []
    for art in articles:
        title = art.get("title") or ""
        description = art.get("description") or ""
        combined = (title or "")
        if description:
            combined = f"{title}. {description}" if title else description

        if combined.strip():
            rows.append({
                "title": title,
                "description": description,
                "text": combined
            })

    if not rows:
        print("🟡 Aucun article exploitable (titres/descriptions vides).")
        sys.exit(0)

    df = pd.DataFrame(rows)

    # S'assurer que les ressources NLTK sont présentes
    ensure_nltk()

    print("🧠 Analyse de sentiment (TextBlob)...")
    df["polarity"] = df["text"].apply(get_polarity)
    df["sentiment"] = df["polarity"].apply(get_sentiment_label)

    # Export CSV
    out_csv = "articles_sentiment.csv"
    df.to_csv(out_csv, index=False)
    print(f"💾 Résultats sauvegardés dans {out_csv}")

    # Visualisation
    counts = df["sentiment"].value_counts()
    plt.figure(figsize=(8, 6))
    counts.plot(kind="bar")
    plt.title("Répartition du sentiment des articles économiques (FR)")
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'articles")
    plt.xticks(rotation=0)
    out_png = "sentiment_graphique.png"
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"🖼️ Graphique sauvegardé dans {out_png}")

    # Affichage console résumé
    print("\n--- Résumé ---")
    print(counts.to_string())
    print("✅ Terminé.")

if __name__ == "__main__":
    main()
