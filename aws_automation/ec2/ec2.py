import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Function to create an EC2 instance
def create_ec2_instance(image_id, instance_type, key_name, security_group_ids, subnet_id):
    try:
        # Run an EC2 instance
        response = ec2_client.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            SecurityGroupIds=security_group_ids,
            SubnetId=subnet_id,
            MinCount=1,
            MaxCount=1
        )

        # Extract instance ID
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 instance with ID '{instance_id}' created successfully.")
        return instance_id
    except Exception as e:
        print("Error creating EC2 instance:", str(e))
        return None

# Main function
def main():
    # EC2 instance details
    image_id = 'ami-1234567890abcdef0'  # Replace with your AMI ID
    instance_type = 't2.micro'
    key_name = 'your-key-pair'  # Replace with your key pair name
    security_group_ids = ['sg-12345678']  # Replace with your security group ID(s)
    subnet_id = 'subnet-12345678'  # Replace with your subnet ID

    # Create an EC2 instance
    instance_id = create_ec2_instance(image_id, instance_type, key_name, security_group_ids, subnet_id)

if __name__ == "__main__":
    main()

