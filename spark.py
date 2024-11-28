from pyspark.sql import SparkSession

# create session
spark = SparkSession.builder \
    .appName("CSV to Temp View") \
    .getOrCreate()


# read files

file_path = "C:/Users/PC/DEprojects/cards_data.csv"
df = spark.read.csv(file_path,header=True,inferSchema=True)

df.createOrReplaceTempView("cards")

result = spark.sql("Select * from cards")

result.show()

spark.stop()
