import boto3

ec2 = boto3.client("ec2")

instance_id = input("Enter EC2 Instance ID to stop: ").strip()

response = ec2.stop_instances(
    InstanceIds=[instance_id]
)

print("\nEC2 stop request sent successfully!")
print("Instance ID:", instance_id)