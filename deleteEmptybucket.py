import boto3

#This code will delete the empty bucket

def delete_empty_buckets(bucket_name):
    s3_client = boto3.client("s3")

    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except Exception as e:
        print(f"Bucket '{bucket_name}' does not exist or you do not have permission to access it.")
        return

    # Check if the bucket is empty
    objects = s3_client.list_objects_v2(Bucket=bucket_name)
    if "Contents" is not objects:
        print(f"Bucket '{bucket_name}' is not empty and cannot be deleted.")
    else:
        try:
            s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Empty bucket '{bucket_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting empty bucket '{bucket_name}': {e}")

if __name__ == "__main__":
    bucket_name_to_delete = "your-empty-bucket-name"
    delete_empty_buckets(bucket_name_to_delete)
