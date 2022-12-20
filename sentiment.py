# Ce fichier comporte toutes les méthodes utilisées pour obtenir un sentiment à partir d'un texte
import eng_spacysentiment

def get_sentiment_score(text):
    # Chargement du modèle de langue avec la librairie eng_spacysentiment
    nlp = eng_spacysentiment.load()

    # Analyse du texte avec spaCy
    doc = nlp(text)

    # Calcul du sentiment final en fonction des scores de positivité et de négativité obtenus par le modèle
    if doc.cats['positive'] > doc.cats['negative']:
        sentiment = "positive"
    elif doc.cats['positive'] < doc.cats['negative']:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment

def get_sentiment_positive(text):
    # Chargement du modèle de langue avec la librairie eng_spacysentiment
    nlp = eng_spacysentiment.load()

    # Analyse du texte avec spaCy
    doc = nlp(text)
    return doc.cats['positive']

def get_sentiment_negative(text):
    # Chargement du modèle de langue avec la librairie eng_spacysentiment
    nlp = eng_spacysentiment.load()

    # Analyse du texte avec spaCy
    doc = nlp(text)
    return doc.cats['negative']


if __name__ == '__main__':
    # Définition du texte à évaluer
    text = "The world is very bad ! Everyone is dying !"

    # Test de la fonction avec le texte "This is a great movie! I loved it."
    #sentiment = get_sentiment(text)
    sentiment_positive = get_sentiment_positive(text)
    sentiment_negative = get_sentiment_negative(text)
    print(f"Le texte '{text}' a un sentiment positif de {sentiment_positive} et negative de {sentiment_negative}.")
