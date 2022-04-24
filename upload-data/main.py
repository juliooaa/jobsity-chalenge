import boto3
import os

## Change ${Path} according to your project path
path = '${Path}/data'
file = 'trips.csv'

print(os.path.join(path, file))   

## Upload data for s3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('chalenge-trips-jobsity')
s3.Object('chalenge-trips-jobsity', 'trips.csv').put(Body=open(os.path.join(path, file), 'rb'))
