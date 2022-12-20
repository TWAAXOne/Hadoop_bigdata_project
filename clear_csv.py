# Ce fichier permet de nettoyer un fichier CSV
from sentiment import *

if __name__ == '__main__':
    # modifie le fichier data.csv pour supprimer les lignes vides et les lignes avec la valeur 'This chart says'
    with open('data.csv', 'r', encoding='latin1') as f:
        lines = f.readlines()
        lines = [line for line in lines if line.strip() != '' and line.strip() != 'This chart says' and len(line.split(',')) == lines[0].count(',') + 1]

        entete = lines[0].strip() # enlève les espaces en début et fin de ligne et les sauts de ligne
        lines[0] = entete + ',sentiment,positive,negative\n'  # ajoute les colonnes sentiment, positive et negative
        indexText = entete.split(',').index('text') # récupère l'index de la colonne text

        for i in range(1, len(lines)):
            valText = lines[i].split(',')[indexText]  # récupère la valeur de la colonne text
            sentiment = get_sentiment_score(valText)  # récupère le sentiment
            positive_score = get_sentiment_positive(valText)  # récupère le score positif
            negative_score = get_sentiment_negative(valText)  # récupère le score négatif

            lines[i] = lines[i].strip() + ',' + sentiment + ',' + str(positive_score) + ',' + str(negative_score) + '\n'
            print(str(i)+'/'+str(len(lines)), repr(lines[i]))  # affiche le numéro de la ligne et la ligne

        with open('data_clear.csv', 'w', encoding='latin1') as f:  # écrit le fichier data_clear.csv
            f.writelines(lines)  # écrit toutes les lignes