import boto3

s3 = boto3.client('s3')
response1 = s3.list_buckets()

# Output the bucket names and locations
print('Existing buckets:')
for bucket1 in response1['Buckets']:
    bucket_name = bucket1['Name']
    location = s3.get_bucket_location(Bucket=bucket_name)
    print(f'  {bucket_name} - {location}')
