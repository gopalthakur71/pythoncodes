import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :condition - doesn't manuvers the directory for the file you provide. File has to be in same directory location. 
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)
        print(f"The item {file_name} is successfully update sans S3 object_name")

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"The item {file_name} successfully updated avec object_name")
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload_file("listS3.py", "agamyathakur17", "listS3.py")