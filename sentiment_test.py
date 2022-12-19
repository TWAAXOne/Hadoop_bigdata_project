import eng_spacysentiment

def get_sentiment_score(text):
    # Chargement du modèle de langue avec la librairie eng_spacysentiment
    nlp = eng_spacysentiment.load()

    # Analyse du texte avec spaCy
    doc = nlp(text)

    # Calcul du sentiment final en fonction des scores de positivité et de négativité obtenus par le modèle
    if doc.cats['positive'] > doc.cats['negative']:
        sentiment = "positif"
    elif doc.cats['positive'] < doc.cats['negative']:
        sentiment = "negatif"
    else:
        sentiment = "neutre"

    return sentiment


if __name__ == '__main__':
    # Définition du texte à évaluer
    text = ""

    # Test de la fonction avec le texte "This is a great movie! I loved it."
    sentiment = get_sentiment_score(text)
    print(f"Le texte '{text}' a un sentiment {sentiment}.")
