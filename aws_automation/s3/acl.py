import boto3

# Initialize the S3 client
s3_client = boto3.client('s3')

# Function to fetch details about an S3 bucket
def fetch_bucket_details(bucket_name):
    try:
        # Get bucket ACL
        acl_response = s3_client.get_bucket_acl(Bucket=bucket_name)
        print(f"ACL for bucket '{bucket_name}':")
        for grant in acl_response['Grants']:
            print(f"Grantee: {grant['Grantee']}, Permission: {grant['Permission']}")

        # Get bucket versioning status
        versioning_response = s3_client.get_bucket_versioning(Bucket=bucket_name)
        status = versioning_response.get('Status', 'Versioning not configured')
        print(f"Versioning status for bucket '{bucket_name}': {status}")

        # Get bucket lifecycle configuration
        lifecycle_response = s3_client.get_bucket_lifecycle_configuration(Bucket=bucket_name)
        rules = lifecycle_response.get('Rules', [])
        if rules:
            print(f"Lifecycle configuration for bucket '{bucket_name}':")
            for rule in rules:
                print(f"Rule ID: {rule.get('ID')}, Prefix: {rule.get('Prefix')}, Expiration: {rule.get('Expiration', 'None')}")
        else:
            print(f"No lifecycle configuration found for bucket '{bucket_name}'")
    except Exception as e:
        print(f"Error fetching details for bucket '{bucket_name}': {str(e)}")

# Main function
def main():
    # Bucket details
    bucket_name = 'your-bucket-name'

    # Fetch details about the bucket
    fetch_bucket_details(bucket_name)

if __name__ == "__main__":
    main()

