#HDFS-Mongo Used to write the json file from HDFS to Mongo DB

from pyspark.sql import SparkSession

my_spark = SparkSession \
         .builder \
         .appName("testdb") \
         .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/testdb.test1") \
         .config("spark.mongodb.output.uri","mongodb://127.0.0.1/testdb.test1") \
         .config('spark.jars.packages', 'org.mongodb.spark:mongo-spark-connector_2.11:2.3.0') \
         .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0')\
         .getOrCreate()


df = my_spark.read.option("multiline", "true").json("hdfs://sandbox-hdp.hortonworks.com:8020/user/root/output2.json")

df.count()

df.printSchema()

df.read.format("com.mongodb.spark.sql.DefaultSource")

df.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").option("database","testdb").option("collection", "test1").save()