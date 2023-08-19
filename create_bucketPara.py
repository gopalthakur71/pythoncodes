import boto3
import pprint

#There can be number of parameter while creating s3 bucket. below are a few. 
s3 = boto3.client("s3")
response = s3.create_bucket(
    ACL="private",      #Acl is private
    Bucket="gopal71s3",   # Bucket name
    CreateBucketConfiguration={"LocationConstraint": "ap-south-1"},   #location 
)
print(pprint.pprint(response))