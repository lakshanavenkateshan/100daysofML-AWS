# Day 26/100 — Machine Learning + AWS + DevOps Journey

## Deployed Fashion-MNIST API on AWS ECS

Today I deployed my **Dockerized Fashion-MNIST Flask API** to the cloud using **AWS ECS (Fargate)**. The API is now publicly accessible and ready for real requests.  

### What I Did
- Pushed the Docker image to **AWS ECR**.  
- Created an **ECS Fargate Task & Cluster**.  
- Verified that the API works live.

### How I Did It
Login to AWS ECR and authenticate Docker:
```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
```
### Create an ECR repository:
```bash
aws ecr create-repository --repository-name fashion-mnist-api
```
### Tag the Docker image for ECR:
```bash
docker tag fashion-mnist-api:latest <account-id>.dkr.ecr.<region>.amazonaws.com/fashion-mnist-api:latest
```
### Push the image to ECR:
```bash
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/fashion-mnist-api:latest
```
In AWS Console, create an ECS Fargate Cluster → Networking only → Name the cluster.

Create a Task Definition: Launch Type Fargate, container name fashion-mnist-api, image URL from ECR, 512MiB memory, 256 CPU, port mapping 5000 → 5000.

Run the ECS Task: select Task Definition, subnet, security group → run.

Test the API live:
curl -X POST http://<public-ip>:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[0,0,0,....,0]}'


### Why I Did It

To move from local development to cloud deployment, making the API accessible anywhere.

To practice AWS DevOps skills, including Docker, ECR, ECS, and networking.

Prepares me for end-to-end MLOps workflows.
