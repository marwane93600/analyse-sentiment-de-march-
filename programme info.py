import requests
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
import ssl

print("Début du script")

# Configurer SSL pour ignorer les erreurs de certificat
ssl._create_default_https_context = ssl._create_unverified_context

# Télécharger les ressources nécessaires pour nltk
nltk.download('punkt')
print("Téléchargement des ressources nltk terminé")

# 1. Récupérer les articles économiques via News API
api_key = '3dabd76f247849919270dee0bf6c251d'  # Ta clé API News API
url = f'https://newsapi.org/v2/everything?q=économie&apiKey={api_key}'

# Effectuer la requête GET à News API
response = requests.get(url)
print("Requête GET effectuée")

# Vérifier que la requête a réussi (code 200)
if response.status_code == 200:
    # Convertir la réponse en JSON
    data = response.json()
    print("Réponse JSON convertie")
   
    if data['status'] == 'ok' and 'articles' in data:
        # Extraire les articles dans une liste
        articles = data['articles']
        print(f"{len(articles)} articles récupérés.")
    else:
        print("Aucun article trouvé.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
    articles = []

# 2. Nettoyer les articles récupérés (extraction des titres et descriptions)
articles_data = []
for article in articles:
    title = article['title']
    description = article['description']
    if title and description:
        articles_data.append({'title': title, 'description': description})

print(f"{len(articles_data)} articles nettoyés et ajoutés à la liste.")

# Imprimer les titres des articles pour vérifier le contenu
for article in articles_data:
    print(f"Titre: {article['title']}")

# Convertir les articles en DataFrame pour mieux gérer les données
df = pd.DataFrame(articles_data)
print("Conversion en DataFrame réussie.")

# 3. Analyser le sentiment des articles (positif, négatif, neutre)
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positif'
    elif polarity < 0:
        return 'Négatif'
    else:
        return 'Neutre'

# Ajouter une colonne pour le sentiment de chaque article
df['sentiment'] = df['description'].apply(get_sentiment)
print("Analyse de sentiment complétée.")

# 4. Créer un graphique pour visualiser le sentiment global
sentiment_counts = df['sentiment'].value_counts()
print("Comptage des sentiments effectué.")

# Création du graphique
plt.figure(figsize=(8,6))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'grey'])
plt.title('Répartition du Sentiment des Articles Économiques')
plt.xlabel('Sentiment')
plt.ylabel("Nombre d'Articles")
plt.xticks(rotation=0)
plt.show()
print("Graphique affiché.")

# Sauvegarder les résultats dans un fichier CSV pour référence
df.to_csv('articles_sentiment.csv', index=False)
print("Résultats sauvegardés dans articles_sentiment.csv.")