import boto3
import os

def upload_directory(path, bucket_name, s3_client):
    for root, dirs, files in os.walk(path):
        for file in files:
            local_path = os.path.join(root, file)
            s3_path = os.path.relpath(local_path, path)
            s3_path = s3_path.replace("\\", "/")  # Replace backslashes with forward slashes for S3 path
            s3_client.upload_file(local_path, bucket_name, s3_path)
            print(f"Uploaded: {s3_path}")

# Set your AWS credentials (replace with your own values)
#access_key = 'YOUR_ACCESS_KEY'
#secret_key = 'YOUR_SECRET_KEY'

# Set the path to the root directory you want to upload
root_directory = 'I:'

# Set your S3 bucket name
bucket_name = 'gopal71s3'

# Create an S3 client
s3_client = boto3.client('s3',)

# Upload the directories and files
upload_directory(root_directory, bucket_name, s3_client)
