
# importing necessary functons
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

#declaring sample python functoin
if __name__=="__main__":
    print("Hey Streaming started")

# stating spark session
spark1 = SparkSession.builder.appName('streaming').getOrCreate()

#first data frame    Read stream
lines_df=spark1.readStream.format("socket").option("host","127.0.0.1").option("port","1679").load()

print(lines_df.isStreaming)
lines_df.printSchema()

#second dataframe or processed dataframe
words_df=lines_df.select(explode(split("value",',')).alias("Word"))

#third dataframe
word_count_df=words_df.groupBy("Word").count()

# writeStream
write_query=word_count_df.writeStream.outputMode("update").format("console").start()

write_query.awaitTermination()
print("Streaming Ended")