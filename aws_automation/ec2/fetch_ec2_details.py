import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Function to fetch details about all EC2 instances
def fetch_ec2_details():
    try:
        # Describe all EC2 instances
        response = ec2_client.describe_instances()

        # Iterate over reservations and instances
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                # Print instance details
                print("Instance ID:", instance['InstanceId'])
                print("Instance Type:", instance['InstanceType'])
                print("Public IP Address:", instance.get('PublicIpAddress', 'N/A'))
                print("Private IP Address:", instance.get('PrivateIpAddress', 'N/A'))
                print("State:", instance['State']['Name'])
                print("Tags:", instance.get('Tags', []))
                print()
    except Exception as e:
        print("Error fetching EC2 details:", str(e))

# Main function
def main():
    # Fetch details about all EC2 instances
    fetch_ec2_details()

if __name__ == "__main__":
    main()

