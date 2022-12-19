from sentiment_test import get_sentiment_score

if __name__ == '__main__':
    # modifie le fichier data.csv pour supprimer les lignes vides et les lignes avec la valeur 'This chart says'
    with open('data.csv', 'r', encoding='latin1') as f:
        lines = f.readlines()
        lines = [line for line in lines if line.strip() != '' and line.strip() != 'This chart says' and len(line.split(',')) == 3]

        # aouter la colonne 'date' au fichier data.csv
        lines[0] = 'sentiment,' + lines[0]
        for i in range(1, len(lines)):
            sentiment = get_sentiment_score(lines[i].split(',')[-1])
            lines[i] = sentiment + ',' + lines[i]
            print(lines[i])

        with open('data_clear.csv', 'w', encoding='latin1') as f:
            f.writelines(lines)