# Au début, nous avons essayé de mettre nos données sur MongoDB. Mais la version HDP est trop ancienne.
# Donc, nous avons décidé d'essayé de mettre notre json dans une table Hive. Mais nous n'avons pas réussit
# Au final, nous avons décidé de transformer notre json en csv et de le mettre manuellement dans Hive.

from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("app") \
    .config("spark.sql.warehouse.dir", "/root/spark-warehouse") \
    .getOrCreate()

print("Récupération des données json depuis HDFS")
df = spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/sortie.json")


df = df.toPandas()  # convert to pandas dataframe
df = df[
    ['id', 'created_at', 'text', 'source', 'geo', 'place', 'retweet_count', 'favorite_count', 'favorited', 'retweeted']]  # select the columns

# get only data from 5 to numbers of rows spark dataframe
df = df.head(df.shape[0] - 5)
df = df.tail(df.shape[0] - 5)
print(df)

df = df.drop_duplicates(subset=['text'])  # suppression des doublons dans texts
print("Conversion en csv")
df.to_csv('data.csv', index=False)
