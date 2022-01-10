import sys
import json
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from pyspark.sql.types import *
import findspark
findspark.init("/opt/spark")
import pyspark

conf = pyspark.SparkConf()
#conf.set('spark.app.name', DataStreamingApp) # Optional configurations

# init & return
sc = pyspark.SparkContext.getOrCreate(conf=conf)
sqlcontext = SQLContext(sc)
spark = SparkSession.builder.appName('WeatherStreamingApp').getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "Data_Streaming") \
  .load()
query = df \
    .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)") \
    .writeStream \
    .format("console") \
    .start()
query.awaitTermination()