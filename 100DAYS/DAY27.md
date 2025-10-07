### Day 27 — Monitoring Dockerized ML API with Prometheus & Grafana 

After deploying, I wanted to see live metrics from my API. Today I set up Prometheus + Grafana monitoring.

### What I Did

Added Prometheus metrics to the Flask API.

Configured Prometheus to scrape the API.

Created a Grafana dashboard to visualize live metrics like request count, latency, and error rates.

### How I Did It

Install Prometheus exporter in Flask:

pip install prometheus-flask-exporter

Update app.py

Prometheus config prometheus.yml

Docker Compose to run Flask + Prometheus + Grafana

### Start everything:

docker-compose up -d

Check Prometheus targets: http://localhost:9090/targets
 → fashion-api should be UP.

Create Grafana dashboard: http://localhost:3000
, login admin/admin → Add Prometheus as data source → Add panels:

flask_http_request_total → Request count

flask_http_request_duration_seconds_sum → Latency

flask_http_request_total{status="200"} → Successful requests

flask_http_request_total{status="500"} → Errors

Send some requests to see live metrics update:

curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[0,0,0,...,0]}'

### Why I Did It

To monitor API performance in real-time.

Helps detect issues, latency, or errors immediately.

Prepares the system for production-ready monitoring, a key DevOps skill.
