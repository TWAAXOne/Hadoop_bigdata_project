#Mongo-HIVE reads MONGO collection and writes into HIVE table

from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext, SparkSession, HiveContext

#conf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")

spark = SparkSession.builder \
        .appName("app") \
        .config("spark.sql.warehouse.dir", "/root/spark-warehouse") \
        .enableHiveSupport() \
        .getOrCreate()

df = spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/sortie.json")

#Database on Hive                                                                                                                                                       
spark.sql("create database IF NOT EXISTS bitcoindb")

print('Voici le Dataframe : ', df)

df.write.mode("overwrite").saveAsTable("bitcoindb.twiterdata")

spark.sql("SHOW DATABASES").show()

df = spark.sql("SELECT id, full_text FROM bitcoindb.twiterdata")
df.show()