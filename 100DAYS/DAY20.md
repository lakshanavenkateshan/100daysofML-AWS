# Day 20 — Deploy Docker Image to AWS ECR & Run on EC2

## Goal
Push the Titanic ML API Docker image to **Amazon Elastic Container Registry (ECR)** and run it from ECR on your EC2 instance.

---

## Step 1 — Create ECR Repository
- Go to **AWS Console → ECR (Elastic Container Registry)**  
- Click **Create repository**  
- Name: `titanic-ml-api`  
- Visibility: **Private**  
- Copy the repository URI (looks like):  


---

## Step 2 — Authenticate Docker with ECR
On your EC2 terminal, run:
```bash
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.ap-south-1.amazonaws.com
```

## Step 3 — Tag and Push Docker Image

Build & tag your image:
```bash
cd ~/CI-CD-Titanic
docker build -t titanic-ml-api .
docker tag titanic-ml-api:latest 123456789012.dkr.ecr.ap-south-1.amazonaws.com/titanic-ml-api:latest
```
Push it to ECR:
```bash
docker push 123456789012.dkr.ecr.ap-south-1.amazonaws.com/titanic-ml-api:latest
```

## Step 4 — Run Container from ECR

Pull & run the image from ECR:
```bash
docker pull 123456789012.dkr.ecr.ap-south-1.amazonaws.com/titanic-ml-api:latest
docker run -d --name titanic-from-ecr -p 5000:5000 123456789012.dkr.ecr.ap-south-1.amazonaws.com/titanic-ml-api:latest
```

## Step 5 — Test API

From your local machine:
```bash
curl -X POST http://<EC2-Public-IP>:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"features\": [3,1,22,0,0,7.25]}"
```
Check logs inside EC2:
```bash
cat /var/log/titanic.log
```
