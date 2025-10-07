# Day 25/100 - Machine Learning + AWS + DevOps Journey

##  Dockerizing My Fashion-MNIST Flask API

Today I containerized my **Fashion-MNIST Flask API**, making it portable and ready for deployment on AWS.  
This is a major step toward building a full MLOps workflow where the ML model runs seamlessly in any environment.

---

###  What I Did:
- Created a **Dockerfile** and **requirements.txt**
- Built a Docker image for the Flask API
- Ran the container on **port 5000**
- Tested model predictions inside the container

---

###  Files Created:

#### **Dockerfile**
```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
```
###  requirements.txt
flask
numpy
scikit-learn
joblib


###  Commands used:

# Step 1 — Build Docker image
docker build -t fashion-mnist-api .

# Step 2 — Run container on port 5000
docker run -d --name fashion-mnist -p 5000:5000 fashion-mnist-api

# Step 3 — Verify running container
docker ps

# Step 4 — Test prediction endpoint
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d "{\"features\": [0,0,0,0,0,0,0,0,0,0,0,0,0,..........]
