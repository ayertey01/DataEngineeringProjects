import os
from pyspark.sql import SparkSession

# Set environment variables for Hadoop and Java
os.environ['HADOOP_HOME'] = "C:/Program Files/hadoop-3.3.6"
os.environ['JAVA_HOME'] = "C:/Program Files/Java/jdk-11"  # Update with your actual Java path

# Create Spark session
spark = SparkSession.builder \
    .appName("TestApp") \
    .config("spark.hadoop.fs.defaultFS", "file:///") \
    .config("spark.sql.warehouse.dir", "/tmp") \
    .getOrCreate()

print("Spark session created successfully!")
