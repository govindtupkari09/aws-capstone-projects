# Project 2 - AWS Resource Automation Using Python

## 📌 Project Overview

This project automates common AWS resource management tasks using Python and the AWS SDK for Python (Boto3).

Instead of manually performing operations through the AWS Management Console, the application provides a simple command-line menu to perform AWS operations programmatically.

The project demonstrates how Python can be used to interact with AWS services securely and efficiently.

---

## 🎯 Objective

The main objective of this project is to automate AWS resource provisioning and management using Python and Boto3.

The application can:

- Create S3 buckets
- Upload files to S3
- Launch EC2 instances
- List EC2 instances
- Stop EC2 instances
- Terminate EC2 instances

---

## 🛠️ Technologies Used

- Python 3
- AWS Boto3
- Amazon S3
- Amazon EC2
- AWS IAM
- AWS CLI
- Git & GitHub
- PowerShell

---

## ☁️ AWS Services Used

### Amazon S3

Used for:

- Creating S3 buckets
- Uploading files

### Amazon EC2

Used for:

- Launching EC2 instances
- Listing instances
- Stopping instances
- Terminating instances

### AWS IAM

Used for authentication and authorization of AWS API requests.

### Boto3

Boto3 is the AWS SDK for Python. It allows Python applications to communicate with AWS services programmatically.

---

## ✨ Features

The application provides a CLI-based menu:

```text
==============================
     AWS RESOURCE AUTOMATOR
==============================
1. Create S3 Bucket
2. Upload File to S3
3. Launch EC2
4. List EC2 Instances
5. Stop EC2 Instance
6. Terminate EC2 Instance
7. Exit