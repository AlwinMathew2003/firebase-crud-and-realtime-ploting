from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import cv2
import os

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# Load the trained model
MODEL_PATH = "high_accuracy_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define image dimensions (same as training)
IMG_HEIGHT = 64
IMG_WIDTH = 64

# Define class labels for all blood groups (+ve and -ve)
CLASS_LABELS = ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"]

# Function to preprocess image
def preprocess_image(image_path):
    image = cv2.imread(image_path)  # Load image
    image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH))  # Resize to model input size
    image = image / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Route to serve HTML page
@app.route("/", methods=["GET"])
def home():
    return render_template("index1.html")

# Route to handle image upload and prediction
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    file_path = "temp.jpg"
    file.save(file_path)

    # Preprocess the image
    image = preprocess_image(file_path)

    # Make prediction
    predictions = model.predict(image)
    predicted_class = CLASS_LABELS[np.argmax(predictions)]

    # Remove temporary file
    os.remove(file_path)

    # Return prediction result
    return jsonify({"predicted_blood_group": predicted_class})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
