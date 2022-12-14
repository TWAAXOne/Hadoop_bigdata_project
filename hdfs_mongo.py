#HDFS-Mongo Used to write the json file from HDFS to Mongo DB

from pyspark.sql import SparkSession

my_spark = SparkSession \
         .builder \
         .appName("MongoDBIntegration") \
         .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/hadoopdb.bitcoin") \
         .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/hadoopdb.bitcoin") \
         .getOrCreate()


df = my_spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/Output2.json")

df.count()

df.printSchema()

df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").option("database","hadoopdb").option("collection", "bitcoin").save()