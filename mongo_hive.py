#Mongo-HIVE reads MONGO collection and writes into HIVE table

from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext, SparkSession, HiveContext
                                                                                                                                                                        
conf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")
                                                                                                                                                                        
                                                                                                                                                                        
spark = SparkSession.builder \
        .appName("test") \
        .getOrCreate()

df = spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/maria_dev/output2.json")

#Database on Hive                                                                                                                                                       
spark.sql("create database testdb")

print('Voici le Dataframe : ', df)

df.write.mode("overwrite").saveAsTable("testdb.test3")

spark.sql("SHOW DATABASES").show()

df = spark.sql("SELECT * FROM testdb.test3")
df.show()