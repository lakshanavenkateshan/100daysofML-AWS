# Day 28/100 — Machine Learning + AWS + DevOps Journey

## Visualized My ML API Metrics in Grafana 

Today I created **real-time dashboards** for my Dockerized Fashion-MNIST API!  

### What I Did
- Integrated **Prometheus** with Flask metrics.  
- Built **Grafana dashboards** to track API performance.  
- Visualized live metrics such as **requests, latency, and status codes**.  

### How I Did It
1. Verified Prometheus was scraping metrics from the Flask API.  
2. Opened Grafana ([http://localhost:3000](http://localhost:3000)) and logged in (`admin/admin`).  
3. Added Prometheus as a **data source**.  
4. Created a **new dashboard**:  
   - Panel 1: `flask_http_request_total` → Total requests  
   - Panel 2: `flask_http_request_duration_seconds_sum` → Latency  
   - Panel 3: `flask_http_request_total{status="200"}` → Successful requests  
   - Panel 4: `flask_http_request_total{status="500"}` → Error requests  
5. Tested live metrics by sending requests to the API:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"features":[0,0,0,...,0]}'
```
### Why I Did It

To monitor API performance in real-time and quickly identify issues.

To practice DevOps skills: monitoring, metrics visualization, and production-grade observability.

Prepares my ML system for scalable deployments and real-world usage.
