import boto3
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

# Function to create a new S3 bucket
def create_bucket(bucket_name, region='us-west-1'):
    try:
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket '{bucket_name}': {str(e)}")

# Function to upload a file to an S3 bucket
def upload_file(bucket_name, file_path, object_key):
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"File '{file_path}' uploaded to '{object_key}' in bucket '{bucket_name}' successfully.")
    except Exception as e:
        print(f"Error uploading file '{file_path}' to '{object_key}' in bucket '{bucket_name}': {str(e)}")

# Function to download a file from an S3 bucket
def download_file(bucket_name, object_key, download_path):
    try:
        s3_client.download_file(bucket_name, object_key, download_path)
        print(f"File '{object_key}' downloaded from bucket '{bucket_name}' to '{download_path}' successfully.")
    except Exception as e:
        print(f"Error downloading file '{object_key}' from bucket '{bucket_name}' to '{download_path}': {str(e)}")

# Function to list all objects in an S3 bucket
def list_objects(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            print(f"Objects in bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f"No objects found in bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Error listing objects in bucket '{bucket_name}': {str(e)}")

# Main function
def main():
    # Bucket details
    bucket_name = 'my-bucket'
    region = 'us-west-1'
    file_path = 'example.txt'
    object_key = 'example.txt'
    download_path = 'downloaded_example.txt'

    # Create a new bucket
    create_bucket(bucket_name, region)

    # Upload a file to the bucket
    upload_file(bucket_name, file_path, object_key)

    # List all objects in the bucket
    list_objects(bucket_name)

    # Download the file from the bucket
    download_file(bucket_name, object_key, download_path)

if __name__ == "__main__":
    main()

