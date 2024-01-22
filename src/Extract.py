# Databricks notebook source
# MAGIC %md
# MAGIC ### Extract

# COMMAND ----------

import pandas as pd
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

my_db=pd.read_csv("../data/UniversalTopSpotifySongs.csv")
spark_db=spark.createDataFrame(my_db)


# COMMAND ----------

csv_file_path=f'/FileStore/tables/{"UniversalTopSpotifySongs"}.csv'
spark_db.write.mode('overwrite').csv(csv_file_path)


# COMMAND ----------

from pyspark.sql.types import DoubleType, StringType, StructType, StructField, LongType

schema = StructType([
  StructField("id", LongType(),  True),
  StructField("spotify_id", StringType(),  True),
  StructField("name", StringType(),  True),
  StructField("artists", StringType(),  True),
  StructField("daily_rank", LongType(),  True),
  StructField("daily_movement", LongType(),  True),
  StructField("weekly_movement", LongType(),  True),
  StructField("country", StringType(),  True),
  StructField("snapshot_date", StringType(),  True),
  StructField("popularity", LongType(),  True),
  StructField("is_explicit", StringType(),  True),
  StructField("duration_ms", LongType(),  True),
  StructField("album_name", StringType(),  True),
  StructField("album_release_date", StringType(),  True),
  StructField("danceability", DoubleType(),  True),
  StructField("energy", DoubleType(),  True),
  StructField("key", LongType(),  True),
  StructField("loudness", DoubleType(),  True),
  StructField("mode", LongType(),  True),
  StructField("speechiness", DoubleType(),  True),
  StructField("acousticness", DoubleType(),  True),
  StructField("instrumentalness", DoubleType(),  True),
  StructField("liveness", DoubleType(),  True),
])

UniversalTopSpotifySongs=spark.read.csv("dbfs:/FileStore/tables/UniversalTopSpotifySongs.csv", header=True, schema=schema)
UniversalTopSpotifySongs.write.mode("overwrite").saveAsTable("RawUniversalTopSpotifySongs")


# COMMAND ----------

# MAGIC %md
# MAGIC ### Save and Display Delta Table
# MAGIC

# COMMAND ----------

delta_file_path = '/FileStore/tables/RawUniversalTopSpotifySongs.delta'
spark_db.write.format("delta").mode("overwrite").save(delta_file_path)
delta_df = spark.read.format("delta").load(delta_file_path)
delta_df.show()
