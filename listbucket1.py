import boto3
from pprint import pprint

#using resources
def list_s3_buckets_using_resource():
    s3 = boto3.resource("s3")
    buckets = s3.buckets.all()
    for bucket in buckets:
        print(bucket)

if __name__ == "__main__":
    list_s3_buckets_using_resource()