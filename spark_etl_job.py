# glue_etl_job.py
import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw telemetry
raw_data = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://mydatalakes3/raw/"]},
    format_options={"multiline": False}
)

# Flatten
df = raw_data.toDF()
df_clean = df.selectExpr("device_id", "timestamp", "temperature", "status")
dyf_clean = DynamicFrame.fromDF(df_clean, glueContext, "dyf_clean")

# Write Parquet
glueContext.write_dynamic_frame.from_options(
    frame=dyf_clean,
    connection_type="s3",
    connection_options={"path": "s3://mydatalakes3/analytics/telemetry/"},
    format="parquet"
)

# Write Avro
glueContext.write_dynamic_frame.from_options(
    frame=dyf_clean,
    connection_type="s3",
    connection_options={"path": "s3://mydatalakes3/machine/telemetry/"},
    format="avro"
)

job.commit()
