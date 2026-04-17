from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

rides_schema = spark.sql('SELECT * FROM cab.bronze.bulk_rides').schema

# Empty Streaming Table
dp.create_streaming_table("stg_rides")  # new table where all the initial and new rides will be appended and stored

# Bulk/Initial Load
@dp.append_flow(
  target = "stg_rides"
  ) 
def rides_bulk():
    df = spark.readStream.table("bulk_rides")
    df = df.withColumn("booking_timestamp", col("booking_timestamp").cast("timestamp"))
    return df 

# Streaming Load
@dp.append_flow(
  target = "stg_rides"
  ) 
def rides_stream():
    df = spark.readStream.table("rides_raw")
    df_parsed = df.withColumn("parsed_rides", from_json(col("rides"), rides_schema))\
                .select("parsed_rides.*")
    df_parsed = df_parsed.withColumn("booking_timestamp", col("booking_timestamp").cast("timestamp"))
    return df_parsed


