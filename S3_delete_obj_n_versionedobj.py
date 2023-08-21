import boto3

def delete_objects(bucket_name):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    for obj in bucket.objects.all():
        obj.delete()

    print(f"All objects in '{bucket_name}' deleted successfully.")

def delete_versioned_objects(bucket_name):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)

    for obj_version in bucket.object_versions.all():
        bucket.delete_objects(
            Delete={
                "Objects": [
                    {
                        "Key": obj_version.object_key,
                        "VersionId": obj_version.id
                    }
                ]
            }
        )

    print(f"All versioned objects in '{bucket_name}' deleted successfully.")

if __name__ == "__main__":
    bucket_name_to_delete_objects = "your-bucket-name"
    bucket_name_to_delete_versioned_objects = "your-versioned-bucket-name"

    delete_objects(bucket_name_to_delete_objects)
    delete_versioned_objects(bucket_name_to_delete_versioned_objects)
