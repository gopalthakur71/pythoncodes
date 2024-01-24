import boto3

def lambda_handler(event, context):
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Get a list of all regions
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        print(f"Checking instances in region: {region}")

        # Create a new EC2 client for the current region
        ec2_client_region = boto3.client('ec2', region_name=region)

        # Describe running instances in the current region
        response = ec2_client_region.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

        # Print instance information
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}, Region: {region}")

    return {
        'statusCode': 200,
        'body': 'Function executed successfully!'
    }
