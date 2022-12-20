# Projet Hadoop - Analyse twitter bitcoin data
Ce repositories contient les informations sur l'analyse des tweets liée au bitcoin générées à l'aide de l'API twitter.

### A propos du projet
Ce projet a pour but d'utiliser plusieurs technologies Hadoop. Telle que HDFS, Kafka, Spark, Hive et Zeppelin. 
1. Récupérer des tweets liés au bitcoin sur Kafka
2. Grace au producer Kafka, transformer les données récupérer en Json. Puis nous les stockons sur HDFS 
3. Spark récupère le json et le range dans un Dataframe. Puis, panda le transforme en CSV.
4. Nettoyer le fichier CSV et ajouter des colonnes liées au sentiment des tweets grâce à un model en machine learning
5. Stocker le fichier CSV sur Hive manuellement
6. Visualiser à l'aide de Zeppelin.
 
### Technogologies utilisées
- Hortonworks HDP - 2.6.5 sandbox from Oracle VM VirtualBox/Vm-ware
- Kafka Server in HDP
- Hive Server in HDP
- Apache Spark Server in HDP
- Apache Zeppelin in HDP

### Problèmes rencontrés
- Problème de connexion à l'API twitter
- Problème avec la version python 2.0
- Problème avec MongoDB, nous avons donc utilisé Hive (mongodb n'est plus compatible avec HDP)
- Problème pour sauvegarder les données sur Hive grâce à spark, donc nous l'avons fait manuellement

### Getting Started
#### Installation
- Télécharger HDP 2.6.5 sandbox from Oracle VM VirtualBox/Vm-ware
- Déposer les fichiers du projet dans le répertoire /root en utilisant Filezilla
  - crypto_producer.py
  - crypto_consumer.py
  - json_to_csv.py
  - clean_csv.py
  - sentiment.py
  - config.ini
  - requirements.txt
- Aller sur port 4200, pour accéder au shell
  - Désintaller les versions précédentes de python et installer python 3
    - yum update
    - yum remove python36u
    - yum install python3
  - Maintenant, il faut installé les dépendances du projet en utilisant la commande suivante:
    - pip3 install --upgrade pip
    - pip3 install -r requirements.txt

#### Lancement des scripts
1. python3 crypto_producer.py
2. python3 crypto_consumer.py
3. python3 json_to_csv.py
4. python3 clean_csv.py
5. Télécharger le CSV "data_clean.csv" avec Filezila et l'upload sur Hive, afin de crée la table "bitcoindb"
6. Lancer Zepplin sur le port 9995, puis cliquer sur "bitcoin_data"


### Remerciement
- [AdharshAla](https://github.com/AdharshAla/covid19_bigdata_project)