DevOps Mini–Project: CI/CD with AWS, Jenkins, and ArgoCD

Objective
Build and deploy a simple application (Python Flask REST API) on AWS using a fully automated CI/CD pipeline with Jenkins and ArgoCD, leveraging the AWS free tier.

Main Components
- Application: Flask API with a /hello endpoint returning "Hello DevOps!".
- GitHub Repository: Hosts source code and Kubernetes manifests.
- AWS Free Tier:
- EKS (Elastic Kubernetes Service) or EC2 + k3s for the Kubernetes cluster.
- Optional S3 bucket for artifact storage.
- Jenkins: Builds and packages the Docker image.
- ArgoCD: Automates deployment to Kubernetes.

Architecture
flowchart TD
    A[GitHub Repo] --> B[Jenkins CI/CD]
    B --> C[Docker Image]
    C --> D[AWS EKS Cluster]
    D --> E[ArgoCD Deployment]
    E --> F[Flask API /hello]


Repository Structure
├── app/
│   └── main.py          # Flask application code
├── Dockerfile           # Docker image definition
├── manifests/
│   └── deployment.yaml  # Kubernetes manifest
├── Jenkinsfile          # CI/CD pipeline
└── README.md            # Documentation


Key Features
- End-to-end automation: From GitHub commit to AWS deployment.
- GitOps workflow: ArgoCD ensures cluster state matches the repository.
- Scalable: Kubernetes manages application lifecycle and scaling.
- Cost-efficient: Built entirely on AWS free tier resources.
  
How to Test
- Clone the repository:
git clone https://github.com/username/devops-mini-project.git
- Run the API locally to test:
cd app
python main.py
- Create Jenkins pipeline and run the build.
- Access at http://localhost:5000/hello.
- Review Jenkins pipeline execution and ArgoCD deployment.
  
Professional Value
This project demonstrates hands-on expertise in:
- CI/CD pipelines with Jenkins
- Containerization using Docker
- Orchestration with Kubernetes
- GitOps practices with ArgoCD
- Cloud deployment on AWS
It serves as a practical showcase of automation, reliability, and modern cloud-native deployment practices—ideal for recruiters and interview discussions.


<img width="724" height="475" alt="image" src="https://github.com/user-attachments/assets/3b4faf97-a109-4170-8336-a7b7eb317030" />
<img width="812" height="541" alt="AWS EC2-DevOps-Diagram" src="https://github.com/user-attachments/assets/15faeb60-687b-4477-bf03-b1655901f857" />
