import boto3
import os

## Change ${Path} according to your project path
path = '${Path}'
file = 'spark.py'

print(os.path.join(path, file))   

## Upload the files to s3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('spark-glue-job')
s3.Object('spark-glue-job', 'spark.py').put(Body=open(os.path.join(path, file), 'rb'))
