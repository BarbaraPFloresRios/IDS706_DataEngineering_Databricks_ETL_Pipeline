# Databricks notebook source
# MAGIC %md
# MAGIC Let's see which artists have the highest presence in the top 50 of Spotify during the evaluation period

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Delta").getOrCreate()

clean_delta_file_path = '/FileStore/tables/CleanUniversalTopSpotifySongs.delta'
clean_delta_df = spark.read.format("delta").load(clean_delta_file_path)

clean_delta_df.createOrReplaceTempView("delta_clean_universal_songs")

query_result = spark.sql("""
    SELECT 
        upper_artists, 
        COUNT(*) AS records_count
    FROM delta_clean_universal_songs
    GROUP BY upper_artists
    ORDER BY records_count DESC
    LIMIT 10
""")

query_result.show()


# COMMAND ----------

# MAGIC %md
# MAGIC Let's check the top Spotify songs for November 5, 2023.

# COMMAND ----------

query_result2 = spark.sql("""
    SELECT 
    country, 
    upper_artists,
    upper_name,
    daily_rank,
    snapshot_date
    FROM delta_clean_universal_songs
    WHERE country = "US" AND snapshot_date = "2023-11-05"
    ORDER BY daily_rank DESC
""")

query_result2.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Let's calculate the Mean Daily Rank Over Time for Top 5 Artists

# COMMAND ----------

query_result3 = spark.sql("""
    SELECT 
    upper_artists,
    snapshot_date,
    mean(daily_rank) as mean_daily_rank
    FROM CleanUniversalTopSpotifySongs
    WHERE upper_artists in ("TAYLOR SWIFT","BAD BUNNY","DOJA CAT","BIZARRAP, MILO J","TATE MCRAE","IÑIGO QUINTERO")
    GROUP BY upper_artists, snapshot_date
""")

query_result3.show()

# COMMAND ----------

import matplotlib.pyplot as plt

db_p = query_result.toPandas()

plt.figure(figsize=(12, 6))
plt.bar(db_p['upper_artists'], db_p['records_count'], color='skyblue')

plt.xticks(rotation=45, ha='right')
plt.xlabel('Artist')
plt.ylabel('Number of Records')
plt.title('Number of Records per Artist')

plt.tight_layout()
plt.show()

# COMMAND ----------

import seaborn as sns

df3 = query_result3.toPandas()
df3 = df3.sort_values(by='snapshot_date')

plt.figure(figsize=(12, 6))
sns.lineplot(x='snapshot_date', y='mean_daily_rank', hue='upper_artists', data=df3)

plt.xticks(rotation=45, ha='right')
plt.legend( loc='upper left')

plt.xlabel('Snapshot Date')
plt.ylabel('Mean Daily Rank')
plt.title('Mean Daily Rank Over Time for Top 5 Artists')

plt.tight_layout()
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC The analysis of the dataset spanning from October 18, 2023, to November 5, 2023, reveals a global music landscape dominated by artists such as "TAYLOR SWIFT," "BAD BUNNY," "DOJA CAT," and others, consistently featured in the top 50 charts of various countries. This suggests not only their widespread appeal but also the existence of diverse musical preferences globally, spanning genres from pop to Latin and urban. The international presence of artists like "BAD BUNNY" and "DOJA CAT" underscores the influence of cross-cultural collaborations on global popularity. Examining the artists' average rankings over time may uncover periodic trends, shedding light on the dynamic nature of music preferences. In essence, this analysis provides a snapshot of the music industry during the specified period, offering insights into both the consistent popularity of certain artists and the ever-evolving global musical landscape.
# MAGIC
# MAGIC
