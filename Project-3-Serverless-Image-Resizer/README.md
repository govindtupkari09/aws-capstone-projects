# Serverless Image Resizer using AWS

## Project Overview

This project is a serverless image processing system that automatically resizes images whenever a new image is uploaded to an Amazon S3 bucket.

The system uses AWS Lambda and Python with the Pillow library to generate multiple image sizes and store them in a separate S3 output bucket.

## Architecture

User
  ↓
Amazon S3 Input Bucket
  ↓
S3 ObjectCreated Event
  ↓
AWS Lambda
  ↓
Pillow Image Processing
  ↓
Amazon S3 Output Bucket
  ├── thumbnail/
  ├── medium/
  └── large/

CloudWatch → Lambda Logs

## AWS Services Used

- Amazon S3
- AWS Lambda
- IAM
- Amazon CloudWatch
- AWS Lambda Layers
- Python
- Pillow

## Input Bucket

```text
serverless-image-resizer-govind-2026