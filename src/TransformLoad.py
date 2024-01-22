# Databricks notebook source
# MAGIC %md
# MAGIC ### Delta Table

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import upper, date_format
spark = SparkSession.builder.appName("Delta").getOrCreate()

delta_file_path = '/FileStore/tables/UniversalTopSpotifySongs.delta'
delta_df = spark.read.format("delta").load(delta_file_path)


clean_delta_df = (delta_df
    .select(
        "id",
        "spotify_id",
        upper("name").alias("upper_name"),
        upper("artists").alias("upper_artists"),
        "daily_rank",
        "daily_movement",
        "weekly_movement",
        "country",
        "snapshot_date",
        "popularity",
        "is_explicit",
        "duration_ms",
        upper("album_name").alias("album_name"),
        date_format("album_release_date", "yyyy-MM-dd").alias("album_release_date"),
        "danceability",
        "energy",
        "key",
        "loudness",
        "mode",
        "speechiness",
        "acousticness",
        "instrumentalness"
    )
)

clean_delta_df.write.format("delta").mode("overwrite").save('/FileStore/tables/CleanUniversalTopSpotifySongs.delta')
clean_delta_df.show()
