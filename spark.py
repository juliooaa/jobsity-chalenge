import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext, DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_timestamp

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "833201630273:glue-database-jobsity", table_name = "chalenge_trips_jobsity", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "833201630273:glue-database-jobsity", table_name = "chalenge_trips_jobsity", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("col0", "string", "region", "string"), ("col1", "string", "origin_coord", "string"), ("col2", "string", "destination_coord", "string"), ("col3", "string", "datetime", "timestamp"), ("col4", "string", "datasource", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("col0", "string", "region", "string"), ("col1", "string", "origin_coord", "string"), ("col2", "string", "destination_coord", "string"), ("col3", "string", "datetime", "timestamp"), ("col4", "string", "datasource", "string")], transformation_ctx = "applymapping1")
## @type: ResolveChoice
## @args: [choice = "make_struct", transformation_ctx = "resolvechoice2"]
## @return: resolvechoice2
## @inputs: [frame = applymapping1]
resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")
## @type: DropNullFields
## @args: [transformation_ctx = "dropnullfields3"]
## @return: dropnullfields3
## @inputs: [frame = resolvechoice2]
dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")

timestampedDf = dropnullfields3.toDF().withColumn("TimeStamp", current_timestamp())
timestamped4 = DynamicFrame.fromDF(timestampedDf, glueContext, 'timestamped4')
## @type: DataSink
## @args: [connection_type = "s3", connection_options = {"path": "s3://chalenge-trips-jobsity/parquet"}, format = "parquet", transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
datasink4 = glueContext.write_dynamic_frame.from_options(frame = timestamped4, connection_type = "s3", connection_options = {"path": "s3://chalenge-trips-jobsity/parquet"}, format = "parquet", transformation_ctx = "datasink4")
job.commit()