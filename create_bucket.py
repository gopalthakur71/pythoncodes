import boto3
import pprint

s3=boto3.client("s3")
response = s3.create_bucket(Bucket="createdfrompython")  #create bucket with default
print(response)