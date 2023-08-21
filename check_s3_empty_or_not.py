import boto3

def is_bucket_empty(bucket_name):
    s3_client = boto3.client("s3")

    # Check if the bucket exists
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except Exception as e:
        print(f"Bucket '{bucket_name}' does not exist or you do not have permission to access it.")
        return False  # Return False if the bucket doesn't exist or access is denied

    # List objects in the bucket
    objects = s3_client.list_objects_v2(Bucket=bucket_name)

    # Check if the bucket is empty
    if "Contents" in objects:
        print(f"Bucket '{bucket_name}' is not empty.")
        return False
    else:
        print(f"Bucket '{bucket_name}' is empty.")
        return True

if __name__ == "__main__":
    # Specify the name of the S3 bucket you want to check
    bucket_name_to_check = "your-bucket-name"

    # Call the function to check if the bucket is empty
    is_empty = is_bucket_empty(bucket_name_to_check)

    if is_empty:
        print(f"The bucket '{bucket_name_to_check}' is empty.")
    else:
        print(f"The bucket '{bucket_name_to_check}' is not empty.")
