# Retrieve the list of existing buckets, acls, versioning and so on. The function below creates a modular approach
# for getting information regarding s3. I can add or remove functions according to the need and can print within for loop. 


import boto3

s3 = boto3.client("s3")
response1 = s3.list_buckets()

'''s3 = boto3.client('s3')
print(type(dir(s3)))'''

def get_bucket_acls(bucket_name):
    acls = s3.get_bucket_acl(Bucket=bucket_name)
    return acls

def get_bucket_versioning(bucket_name):
    versioning = s3.get_bucket_versioning(Bucket=bucket_name)
    return versioning

def get_bucket_encryption(bucket_name):
    encryption = s3.get_bucket_encryption(Bucket=bucket_name)
    return encryption

# ... other functions for other metadata

print('Existing buckets:')
for bucket1 in response1['Buckets']:
    bucket_name = bucket1['Name']
    location = s3.get_bucket_location(Bucket=bucket_name)
    #acls = get_bucket_acls(bucket_name)
    #versioning = get_bucket_versioning(bucket_name)

    # Print the desired information
    print(f'  {bucket_name} - {location}')
    #print(f'    ACLs: {acls}')
    #print(f'    Versioning: {versioning}')
    # ... print other metadata using respective functions

