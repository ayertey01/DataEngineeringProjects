import os
from pyspark.sql import SparkSession

os.environ["HADOOP_HOME"] = "C:/Program Files/hadoop-3.3.6"
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-11"

# create session
spark = SparkSession.builder.getOrCreate()


# read files

file_path = "C:/Users/PC/DEprojects/cards_data.csv"
df = spark.read.csv(file_path,header=True,inferSchema=True)

df.createOrReplaceTempView("cards")

result = spark.sql("Select * from cards")

result.show()

spark.stop()
