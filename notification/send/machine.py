#django libraries
from django.shortcuts import render, redirect
from .models import  AnimalReport
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

#machine learning libraries
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib  # For model persistence (save and load)


#main programs starts here
def preprocess_image(image_path):
    # Add your image preprocessing logic here
    # Example: Load the image, resize, normalize, etc.
    img_width, img_height = 150, 150  # Define image dimensions
    return np.random.random((img_width, img_height, 3)).flatten()  # Flatten the image

def train_model(train_dir):
    # Define image dimensions
    img_width, img_height = 150, 150

    # Load and preprocess the data
    data = []
    labels = []

    for label in os.listdir(train_dir):
        label_path = os.path.join(train_dir, label)
        for image_file in os.listdir(label_path):
            image_path = os.path.join(label_path, image_file)
            img_array = preprocess_image(image_path)
            data.append(img_array)
            labels.append(label)

    # Convert labels to numeric values
    label_encoder = LabelEncoder()
    labels_encoded = label_encoder.fit_transform(labels)

    # Split the data into training and validation sets
    X_train, _, y_train, _ = train_test_split(data, labels_encoded, test_size=0.2, random_state=42)

    # Train a RandomForestClassifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model and label encoder
    joblib.dump(model, 'emotion_classifier_model.pkl')
    joblib.dump(label_encoder, 'label_encoder.pkl')

    print("Model training completed.")

def predict_emotion(image_path):
    model = joblib.load('emotion_classifier_model.pkl')
    label_encoder = joblib.load('label_encoder.pkl')  # Load label encoder
    img_array = preprocess_image(image_path)
    img_array = img_array.reshape(1, -1)  # Reshape to 2D array
    predicted_label = model.predict(img_array)[0]
    predicted_emotion = label_encoder.inverse_transform([predicted_label])[0]
    return predicted_emotion

# directory for training the model
train_dir = 'D:/DjangoProjects/Emotions'

# Verify that the entered directory exists
# if not os.path.exists(train_dir):
#     print(f"The specified directory '{train_dir}' does not exist. Please provide a valid path.")
#     exit()

# Train the model
train_model(train_dir)

# Ask the user to enter the image path for prediction

# Verify that the entered image path exists
# if not os.path.exists(image_path):
#     print(f"The specified image path '{image_path}' does not exist. Please provide a valid path.")
#     exit()

# Make a prediction
