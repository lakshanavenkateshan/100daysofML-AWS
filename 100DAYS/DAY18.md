# Titanic ML App — CI/CD Deployment on AWS with Docker

This guide explains how to deploy a Flask-based Titanic Machine Learning API on AWS EC2 using Docker and automate deployment with GitHub Actions CI/CD.

---

## Step 1 — Create `requirements.txt` (LOCAL)

flask
joblib
scikit-learn
numpy


---

## Step 2 — Update `Dockerfile`

FROM python:3.10-slim
WORKDIR /app
COPY app.py titanic_rf_model.pkl requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]


---

## Step 3 — Create IAM User for CI/CD (AWS Console)

1. Go to **IAM → Users → Add User**  
2. Name: `github-actions`  
3. Enable **Programmatic access**  
4. Attach policies:  
   - `AmazonEC2FullAccess`  
   - `AmazonECRFullAccess`  
5. Save **Access Key ID** & **Secret Access Key** (needed for GitHub secrets)

---

## Step 4 — Add GitHub Secrets

Go to **GitHub repo → Settings → Secrets → Actions** and add:

- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_REGION` (e.g., `ap-south-1`)  
- `AWS_ACCOUNT_ID`  
- `EC2_HOST` (your EC2 public IP or DNS)  
- `EC2_USER` (usually `ubuntu`)  
- `EC2_KEY` (private SSH key content from your `.pem` file)

---

## Step 5 — GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

name: Deploy Titanic ML App

on:
push:
branches: [ "main" ]

jobs:
build-and-deploy:
runs-on: ubuntu-latest

yaml
Copy code
steps:
- name: Checkout code
  uses: actions/checkout@v3

- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: ${{ secrets.AWS_REGION }}

- name: Login to Amazon ECR
  run: |
    aws ecr get-login-password --region ${{ secrets.AWS_REGION }} \
    | docker login --username AWS --password-stdin ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com

- name: Build Docker image
  run: |
    docker build -t titanic-flask-app .

- name: Tag Docker image
  run: |
    docker tag titanic-flask-app:latest ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/titanic-flask-app:latest

- name: Push Docker image to Amazon ECR
  run: |
    docker push ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/titanic-flask-app:latest

- name: Deploy on EC2
  uses: appleboy/ssh-action@v1.0.3
  with:
    host: ${{ secrets.EC2_HOST }}
    username: ${{ secrets.EC2_USER }}
    key: ${{ secrets.EC2_KEY }}
    script: |
      docker pull ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/titanic-flask-app:latest
      docker stop titanic || true
      docker rm titanic || true
      docker run -d --name titanic -p 5000:5000 --restart unless-stopped ${{ secrets.AWS_ACCOUNT_ID }}.dkr.ecr.${{ secrets.AWS_REGION }}.amazonaws.com/titanic-flask-app:latest


---

## Step 6 — Test CI/CD

1. Push your code to GitHub `main` branch.  
2. GitHub Actions will automatically trigger:
   - Build Docker image  
   - Push to ECR  
   - Deploy on EC2  

3. Verify API is running:

curl -X POST http://<ec2-ip>:5000/predict
-H "Content-Type: application/json"
-d '{"features":[3,1,22,0,0,7.25]}'

You should get the predicted survival response from the Titanic ML model.

---

## Notes

- Ensure your EC2 security group allows port **5000** for testing.  
- Workflow will automatically redeploy whenever you push to `main`.  
- Use the `docker logs titanic` command on EC2 for troubleshooting.
