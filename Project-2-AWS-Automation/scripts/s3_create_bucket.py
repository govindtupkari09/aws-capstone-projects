import boto3
from datetime import datetime

s3 = boto3.client("s3")

bucket_name = f"aws-capstone-automation-govind-{datetime.now().strftime('%Y%m%d%H%M%S')}"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "ap-south-1"
    }
)

print("\nS3 bucket created successfully!")
print("Bucket name:", bucket_name)