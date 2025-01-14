import pyspark.sql.functions as F
from pyspark.sql import SparkSession

import logging

spark = SparkSession.builder.appName(
    "Ch03 - Analyzing the vocabulary of Pride and Prejudice. - short"
).getOrCreate()

book = spark.read.text("/opt/spark/data/pride-and-prejudice.txt")

results = (
    book.select(F.split(F.col("value"), " ").alias("line"))
    .select(F.explode(F.col("line")).alias("word"))
    .select(F.lower(F.col("word")).alias("word_lower"))
    .select(F.regexp_extract(F.col("word_lower"), "[a-z]*", 0).alias("word"))
    .where(F.col("word") != "")
    .groupby(F.col("word"))
    .count()
)

logging.info('TEST')

results.orderBy(F.col("count").desc()).show(10)

results.coalesce(1).write.csv("/opt/spark/data/results/chapter03/simple_count.csv")
results.cache()
results.show(20, False)
