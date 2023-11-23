# importing necessary functons
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

#declaring sample python functoin
if __name__=="__main__":
    print("FileStreaming Started")

# stating spark session
spark2 = SparkSession.builder.appName('FileStreaming').getOrCreate()

#schema of the csv file colums
Schema = StructType(
    [StructField("company",StringType(),True),
    StructField("body-style",StringType(), True),
    StructField("length",FloatType(),True),
    StructField("engine",StringType(),True),
    StructField("mileage",IntegerType(),True),
    StructField("sunroof",StringType(),True)]
)

read_df = spark2.readStream.format('csv').schema(Schema).option('header',True).load(path="hdfs://cdhserver:8020/user/labuser/")

#print schema
read_df.printSchema()

#start the stream fetch and display
write_query = read_df.writeStream.outputMode("update").format("console").start()
write_query.awaitTermination()

print("Streaming Done")






