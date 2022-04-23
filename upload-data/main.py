import boto3
import os

path = '/home/juliooliveira/Área de Trabalho/julio/chalenge/upload-data/data'
file = 'trips.csv'

print(os.path.join(path, file))   

s3 = boto3.resource('s3')
bucket = s3.Bucket('chalenge-trips-jobsity')
s3.Object('chalenge-trips-jobsity', 'trips.csv').put(Body=open(os.path.join(path, file), 'rb'))