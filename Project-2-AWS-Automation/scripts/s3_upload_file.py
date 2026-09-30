import boto3
import os

s3 = boto3.client("s3")

bucket_name = input("Enter S3 bucket name: ").strip()
file_name = input("Enter local file name: ").strip()

if not os.path.exists(file_name):
    print("\nError: File not found!")
else:
    s3.upload_file(file_name, bucket_name, os.path.basename(file_name))

    print("\nFile uploaded successfully!")
    print("File:", os.path.basename(file_name))
    print("Bucket:", bucket_name)