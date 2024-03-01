import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

# List all S3 buckets
response = s3_client.list_buckets()

# Print bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(bucket['Name'])

