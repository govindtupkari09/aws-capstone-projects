\# AWS Scalable Web Application



\## 1. Project Title



\*\*Scalable Web Application using Amazon EC2, Application Load Balancer, Auto Scaling Group and CloudWatch\*\*



\---



\## 2. Overview



This project demonstrates how to deploy a highly available and scalable web application on AWS using multiple Amazon EC2 instances.



The application is accessed through an \*\*Application Load Balancer (ALB)\*\*, which distributes incoming HTTP traffic across healthy EC2 instances registered in a Target Group.



An \*\*Auto Scaling Group (ASG)\*\* is used to maintain the required number of EC2 instances, while \*\*Amazon CloudWatch\*\* is used to monitor CPU utilization and create alarms.



The web page displays instance-specific information such as:



\- Hostname

\- Instance ID

\- Private IP address

\- Availability Zone

\- Running status



This makes it possible to visually demonstrate traffic distribution between EC2 instances.



\---



\## 3. Objectives



The main objectives of this project are:



\- Launch and configure an Amazon EC2 web server.

\- Install and configure Apache Web Server.

\- Create an Amazon Machine Image (AMI).

\- Create an EC2 Launch Template.

\- Create an Auto Scaling Group.

\- Configure an Application Load Balancer.

\- Create and configure a Target Group.

\- Distribute HTTP traffic across multiple EC2 instances.

\- Configure EC2 and ALB security groups.

\- Monitor EC2 CPU utilization using Amazon CloudWatch.

\- Create a CloudWatch CPU utilization alarm.

\- Demonstrate a scalable AWS web application architecture.



\---



\## 4. AWS Services Used



| AWS Service | Purpose |

|---|---|

| Amazon EC2 | Hosts the web application |

| Amazon Machine Image (AMI) | Provides a reusable server image |

| EC2 Launch Template | Defines configuration for new instances |

| Auto Scaling Group | Maintains and manages EC2 instances |

| Application Load Balancer | Distributes incoming HTTP traffic |

| Target Group | Registers and health-checks EC2 instances |

| Amazon CloudWatch | Monitors EC2 metrics and CPU utilization |

| Amazon VPC | Provides networking infrastructure |

| Security Groups | Controls inbound and outbound traffic |



\---



\## 5. Architecture Diagram



```text

&#x20;                        Internet / User

&#x20;                               |

&#x20;                               |

&#x20;                        HTTP : Port 80

&#x20;                               |

&#x20;                               v

&#x20;                 +--------------------------+

&#x20;                 | Application Load        |

&#x20;                 | Balancer (ALB)           |

&#x20;                 +------------+-------------+

&#x20;                              |

&#x20;                              v

&#x20;                   +----------------------+

&#x20;                   |    Target Group      |

&#x20;                   |    HTTP : 80         |

&#x20;                   +----------+-----------+

&#x20;                              |

&#x20;               +--------------+--------------+

&#x20;               |              |              |

&#x20;               v              v              v

&#x20;         +-----------+  +-----------+  +-----------+

&#x20;         | EC2       |  | EC2       |  | EC2       |

&#x20;         | Instance  |  | Instance  |  | Instance  |

&#x20;         +-----------+  +-----------+  +-----------+

&#x20;               ^              ^              ^

&#x20;               |              |              |

&#x20;               +--------------+--------------+

&#x20;                              |

&#x20;                              v

&#x20;                   Auto Scaling Group

&#x20;                              |

&#x20;                              v

&#x20;                      Amazon CloudWatch

&#x20;                   CPU Monitoring / Alarm

