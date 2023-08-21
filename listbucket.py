import boto3
from pprint import pprint

#Using client

def list_s3_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response.get("Buckets")
    for bucket in buckets:
        pprint(bucket["Name"])


if __name__ == "__main__":
    list_s3_buckets()