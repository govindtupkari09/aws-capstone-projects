# AWS Capstone Projects

A collection of hands-on AWS Cloud projects covering scalability, automation, serverless architecture, CI/CD, and containerization.

## Projects

| # | Project | Main Technologies |
|---|---|---|
| 1 | Scalable Web Application | EC2, ALB, Auto Scaling, CloudWatch |
| 2 | AWS Resource Automation | Python, Boto3, EC2, S3, IAM |
| 3 | Serverless Image Resizer | S3, Lambda, Python, Pillow, CloudWatch |
| 4 | Node.js CI/CD Pipeline | Node.js, GitHub Actions, EC2, Nginx, PM2 |
| 5 | Docker + ECS Application | Docker, ECR, ECS, Fargate, Flask |

## Project 1 - Scalable Web Application

Build a scalable web application using Amazon EC2, Application Load Balancer and Auto Scaling.

**Services:** EC2, ALB, Target Group, Auto Scaling Group, CloudWatch, IAM.

**Working:** User requests go to the Application Load Balancer. ALB distributes traffic across healthy EC2 instances. Auto Scaling manages the number of instances based on demand, while CloudWatch provides monitoring.

## Project 2 - AWS Resource Automation

Automate AWS resource operations using Python and Boto3.

**Services/Technologies:** Python, Boto3, EC2, S3, IAM, AWS CLI.

**Working:** Python scripts communicate with AWS services through the Boto3 SDK and automate common resource management operations.

## Project 3 - Serverless Image Resizer

Automatically resize images whenever a new image is uploaded to Amazon S3.

**Services/Technologies:** S3, Lambda, IAM, CloudWatch, Python, Pillow.

**Working:** An image uploaded to the S3 input bucket triggers Lambda through an Object Created event. Lambda uses Python and Pillow to create Thumbnail, Medium and Large versions and stores them in the output S3 bucket. CloudWatch is used for monitoring.

**Image Sizes:**
- Thumbnail: 150 x 150
- Medium: 500 x 500
- Large: 1000 x 1000

## Project 4 - Node.js CI/CD Pipeline

Build and deploy a Node.js application using an automated CI/CD workflow.

**Technologies/Services:** Node.js, Express.js, GitHub, GitHub Actions, EC2, Nginx, PM2.

**Working:** Code is stored in GitHub. GitHub Actions runs tests after code changes. After successful testing, the application is deployed to EC2. PM2 keeps the application running and Nginx works as a reverse proxy.

## Project 5 - Docker + ECS Flask Application

Containerize a Python Flask application using Docker and deploy it using Amazon ECS with AWS Fargate.

**Technologies/Services:** Python, Flask, Docker, ECR, ECS, Fargate, IAM, VPC, Security Groups.

**Working:** The Flask application is packaged into a Docker image, pushed to Amazon ECR, and deployed as an ECS Fargate task.

## Skills Demonstrated

- Amazon EC2
- Amazon S3
- AWS Lambda
- IAM
- CloudWatch
- Application Load Balancer
- Auto Scaling
- Python
- Boto3
- Node.js
- GitHub Actions
- Docker
- Amazon ECR
- Amazon ECS
- AWS Fargate
- Linux
- Nginx
- PM2
- Flask

## Repository Structure

aws-capstone-projects/
- Project-1-Scalable-Web-App/
- Project-2-AWS-Automation/
- Project-3-Serverless-Image-Resizer/
- Project-4-CICD-NodeJS/
- Project-5-Docker-ECS/

## Author

**Govind Tupkari**

AWS Cloud / DevOps Enthusiast
