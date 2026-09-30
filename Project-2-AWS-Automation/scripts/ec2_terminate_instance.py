import boto3

ec2 = boto3.client("ec2")

instance_id = input("Enter EC2 Instance ID to terminate: ").strip()

confirmation = input(
    f"Are you sure you want to terminate {instance_id}? (yes/no): "
).strip().lower()

if confirmation == "yes":
    ec2.terminate_instances(
        InstanceIds=[instance_id]
    )

    print("\nEC2 termination request sent successfully!")
    print("Instance ID:", instance_id)

else:
    print("\nTermination cancelled.")