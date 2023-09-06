from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Read the dataset from the CSV file
dt = pd.read_csv('./data/vets_data.csv')

# Initialize a LabelEncoder to encode the 'City' column
enc = LabelEncoder()
enc.fit(['Delhi', 'Gurgaon', 'Noida', 'Faridabad'])

# Encode the 'City' column in the dataset
dt['City'] = enc.transform(dt['City'])

# Separate the features (X) and target variable (y)
X = dt.drop(columns=['Vet'])
y = dt.drop(columns=['City', 'Sector'])

# Initialize a Decision Tree classifier
c_model = DecisionTreeClassifier()
c_model.fit(X, y)

# Function to recommend a veterinarian based on city and sector


def vet_rec(city, sec):
    # Transform the city value using the LabelEncoder
    city = enc.transform([city])

    # Predict the veterinarian using the trained model
    vet = c_model.predict([[city, sec]])

    return vet[0]
