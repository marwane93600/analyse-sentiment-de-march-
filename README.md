# Analyse de sentiment d’articles économiques

Ce projet a pour objectif d’analyser le **sentiment global** des articles récents liés à l’économie, en utilisant **Python** et quelques bibliothèques simples de data science.

L’idée est de voir si les articles traitant d’économie ont un ton plutôt **positif, neutre ou négatif**.

---

## Objectif du projet

Ce travail a été réalisé dans le cadre de ma formation en **CMI D3S – Data Science for Social Sciences** à l’Université Paris Nanterre.

L’objectif est de pratiquer :
- La **récupération de données en ligne** (API NewsAPI)
- Le **nettoyage et l’analyse de texte**
- L’**utilisation d’outils Python** de data science
- La **visualisation des résultats**

---

## Méthodologie

1. **Récupération des articles** via l’API [NewsAPI](https://newsapi.org)
2. **Nettoyage du texte** (titres + descriptions)
3. **Analyse du sentiment** à l’aide de `TextBlob`
4. **Visualisation** des résultats avec `matplotlib`
5. **Export** des résultats dans un fichier CSV et une image

---

## Installation

1. Clonez le dépôt ou téléchargez le projet :
   ```bash
   git clone https://github.com/marwane93600/analyse-sentiment-de-march-.git
