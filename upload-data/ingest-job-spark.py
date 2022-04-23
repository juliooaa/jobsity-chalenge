import boto3
import os

path = '/home/juliooliveira/Área de Trabalho/julio/chalenge'
file = 'spark.py'

print(os.path.join(path, file))   

s3 = boto3.resource('s3')
bucket = s3.Bucket('spark-glue-job')
s3.Object('spark-glue-job', 'spark.py').put(Body=open(os.path.join(path, file), 'rb'))