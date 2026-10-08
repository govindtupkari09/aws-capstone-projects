# Project 5 – Containerized Flask Application on AWS ECS

## 📌 Project Overview

This project demonstrates how to containerize a Python Flask application using Docker and deploy it on Amazon ECS using AWS Fargate.

The Docker image is stored in Amazon ECR, and Amazon ECS runs the container using Fargate.

The application provides a simple home page and a health-check endpoint.

---

## 🏗️ Architecture

```text
                    Internet
                       │
                       ▼
              Public IP of ECS Task
                       │
                       │ TCP : 5000
                       ▼
              ┌───────────────────┐
              │   AWS ECS Cluster │
              │ project-5-cluster │
              └─────────┬─────────┘
                        │
                        ▼
                ┌───────────────┐
                │ AWS Fargate   │
                │               │
                │ Docker        │
                │ Container     │
                │               │
                │ Flask App     │
                │ Port 5000     │
                └───────┬───────┘
                        │
                        │ Docker Image
                        ▼
                ┌───────────────┐
                │ Amazon ECR    │
                │               │
                │ project-5-    │
                │ flask         │
                └───────────────┘