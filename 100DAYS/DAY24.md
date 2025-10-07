# Day 24/100 - Machine Learning + AWS + DevOps Journey 

##  Visualizing the Fashion-MNIST Dataset

Today I explored and visualized the **Fashion-MNIST** dataset — one of the most popular benchmarks in computer vision.  
Even though the images are just **28×28 grayscale pixels**, they represent real-world fashion items like shirts, shoes, and bags.  
It’s fascinating how simple pixel matrices can help ML models classify items into **10 different fashion categories**.

---

###  What I Did:
- Loaded the Fashion-MNIST dataset using `tensorflow.keras.datasets.fashion_mnist`
- Visualized sample images with their corresponding labels
- Checked model predictions for a test image

---

###  Commands Used:

```bash
# Step 1 — Load and visualize dataset
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
plt.imshow(X_test[0], cmap='gray')
plt.title(f"Label: {y_test[0]}")
plt.show()

# Step 2 — Check prediction for a sample image
import joblib
model = joblib.load('fashion_mnist_model.pkl')
y_pred = model.predict(X_test[0].reshape(1, -1))
print("Predicted:", y_pred[0])
print("Actual:", y_test[0])
