import logging
import boto3
from botocore.exceptions import ClientError


def delete_bucket(bucket_name, region=None):

    # Delete bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Bucket deleted as {bucket_name} in default region ")
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.delete_bucket(Bucket=bucket_name)

            print(f"Bucket with {bucket_name} deleted in {region} successfully")
    except ClientError as e:
        return False
    return True

#delete_bucket("ahjvbkndaj", "us-east-2")
delete_bucket("agamyathakur17", "us-west-1")