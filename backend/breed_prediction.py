from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing import image
import numpy as np
import csv

# Load the pre-trained model
model = load_model('./model/model_pretrained_DenseNet.h5')

# Function to preprocess the image


def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0
    return img

# Function to load breeds from a CSV file


def load_breeds_from_csv(file_path):
    breeds = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            breed = row['breed']
            breeds[id] = breed
    return breeds

# Function to predict the breed of a dog from an image


def predict_breed(image_path):
    # Preprocess the image
    img = preprocess_image(image_path)

    # Make the prediction
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction)

    # Load the breed data from the CSV file
    breeds = load_breeds_from_csv('./data/breed_data.csv')

    # Get the predicted breed
    breed = breeds.get(predicted_class)
    return breed
