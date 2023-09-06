import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Path to the data files
DATA_PATH = "./data/disease_data.csv"
DESCRIPTIONS_PATH = "./data/disease_description_data.csv"
DIETS_PATH = "./data/disease_diet_data.csv"

# Read the data files into pandas DataFrames
data = pd.read_csv(DATA_PATH).dropna(axis=1)
descriptions = pd.read_csv(DESCRIPTIONS_PATH).dropna()
diets = pd.read_csv(DIETS_PATH, sep=",")

# Initialize a LabelEncoder for encoding the target variable
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Split the data into features (X) and target variable (y)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=24)

# Get the list of symptoms
symptoms = X.columns.values

# Create a dictionary to map symptoms to their indices
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

# Create a dictionary containing symptom index mapping and predicted classes
data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}

# Initialize a Random Forest classifier
final_rf_model = RandomForestClassifier(random_state=18)
final_rf_model.fit(X, y)

# Function to predict the disease based on given symptoms


def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    # Initialize input data with zeros
    input_data = [0] * len(data_dict["symptom_index"])

    # Set the corresponding symptom indices to 1
    for symptom in symptoms:
        index = data_dict["symptom_index"].get(symptom.capitalize())
        if index is not None:
            input_data[index] = 1

    # Reshape the input data for prediction
    input_data = np.array(input_data).reshape(1, -1)

    # Make the prediction using the trained Random Forest model
    rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[
        0]]

    return rf_prediction

# Function to get the description of a disease


def getDiseaseDescription(rf_prediction):
    # Retrieve the description for the predicted disease
    description = descriptions.loc[descriptions["Disease"]
                                   == rf_prediction, "Description"].values
    if len(description) > 0:
        return description[0]
    else:
        return "Description not available."

# Function to get the diet recommendation for a disease


def getDietRecommendation(rf_prediction):
    # Retrieve the diet recommendation for the predicted disease
    diet = diets.loc[diets["Condition"] ==
                     rf_prediction, "Recommended Diet"].values
    if len(diet) > 0:
        return diet[0]
    else:
        return "Diet recommendation not available."
