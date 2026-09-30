# Deployment Guide

## 1. Architecture
User ? Application Load Balancer ? Target Group ? EC2 Instances

## 2. EC2
- Ubuntu Server 24.04 LTS
- Instance type: t3.micro
- Apache Web Server
- Port: 80

## 3. Target Group
- Name: alb-demo-tg
- Protocol: HTTP
- Port: 80
- Health Check Path: /

## 4. Application Load Balancer
- Name: alb-demo-lb
- Scheme: Internet-facing
- Listener: HTTP : 80
- Traffic forwarded to: alb-demo-tg

## 5. Auto Scaling Group
- Name: alb-demo-asg
- Minimum: 2
- Desired: 2
- Maximum: 3
- Availability Zones: ap-south-1a, ap-south-1b

## 6. CloudWatch
- Metric: CPUUtilization
- Threshold: CPU > 70%
- Evaluation period: 5 minutes
- Alarm: alb-demo-high-cpu

## 7. Testing
The application was tested through the ALB DNS name. Multiple EC2 instances were observed through the application response, demonstrating load balancing.

## 8. Security
- SSH access restricted to the administrator's IP.
- EC2 HTTP access should be restricted to the ALB Security Group.
- AWS credentials, private keys and secrets must never be committed to GitHub.
