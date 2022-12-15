#Mongo-HIVE reads MONGO collection and writes into HIVE table

from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext, SparkSession, HiveContext
from pyspark.sql.functions import col,explode
import requests
import pandas
                                                                                                                                                                        
conf = SparkConf().set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")
                                                                                                                                                                        
                                                                                                                                                                        
spark = SparkSession.builder \
        .appName("test") \
        .getOrCreate()
        # .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/testdb.test1") \
        # .config("spark.mongodb.output.uri","mongodb://127.0.0.1/testdb.test1") \
        # .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.3.2') \
        # .config("spark.sql.warehouse.dir", "/root/spark-warehouse") \
        #.enableHiveSupport() \

                                                                                                                                                                        
#sqlContext = SQLContext(spark.sparkContext)

df = spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/output2.json")
                                                                                                                                                                        
#df = sqlContext.read.format("com.mongodb.spark.sql.DefaultSource").option("uri","mongodb://localhost/testdb.test1").load()
                                                                                                                                                                        
#df.printSchema()

#spark.sql("drop database testdb")
                                                                                                                                                                        
#Database on Hive                                                                                                                                                       
spark.sql("create database testdb")

print('Voici le Dataframe : ', df)

df.write.mode("overwrite").saveAsTable("testdb.test2")

spark.sql("SHOW DATABASES").show()