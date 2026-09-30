import boto3

ec2 = boto3.client("ec2")

ami_id = "ami-007b1f3fdea0383d9"
subnet_id = "subnet-0d9cc365709ae507b"
security_group_id = "sg-0651f22eb26107d0f"
key_name = "aws-capstone-2026-key"

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName=key_name,
    SecurityGroupIds=[security_group_id],
    SubnetId=subnet_id
)

instance_id = response["Instances"][0]["InstanceId"]

print("\nEC2 instance launched successfully!")
print("Instance ID:", instance_id)