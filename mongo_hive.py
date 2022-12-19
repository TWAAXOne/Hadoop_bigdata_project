#Mongo-HIVE reads MONGO collection and writes into HIVE table

from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext, SparkSession, HiveContext
#from datasets import load_dataset
import pandas as pd
import csv

#conf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")

spark = SparkSession.builder \
        .appName("app") \
        .config("spark.sql.warehouse.dir", "/root/spark-warehouse") \
        .getOrCreate()

df = spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/sortie.json")

df2 = df.toPandas()

print("le type est : ", type(df))

df3 = df2[['id', 'created_at' , 'text']]

print("TRuc : ", df3.head(df3.shape[0]-5))
# get only data from 5 to 522 rows spark dataframe
df4 = df3.head(df3.shape[0]-5)

df5 = df4.tail(df4.shape[0]-5)

# print df5
print(df5)

df5.to_csv('data.csv', index=False)





