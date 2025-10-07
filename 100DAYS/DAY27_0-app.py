from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import joblib, numpy as np

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Exposes /metrics

model = joblib.load("fashion_mnist_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    x = np.array(data['features']).reshape(1, -1)
    y_pred = model.predict(x)
    return jsonify({'prediction': int(y_pred[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
