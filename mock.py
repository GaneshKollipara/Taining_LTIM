from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("mock").getOrCreate()

network=spark.read.csv("/home/labuser/Downloads/network.csv",header=True)
series=spark.read.csv("/home/labuser/Downloads/series.csv",header=True)

def filter_network(series, network):
    fil=network.join(series,on="series_id",how="inner")
    return  fil.show()

def full_name_network(network, series):
    pass

def series_with_highest_rating(series):
    pass

def sum_of_ratings_int(series):
    pass

def sum_of_ratings_float(series):
    pass