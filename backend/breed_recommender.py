import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Function to recommend a dog breed based on user input


def breed_recommendation(form_data):
    # Load the CSV file
    data = pd.read_csv('./data/doggo_features.csv')

    # Drop rows with missing values
    data = data.dropna()

    # Split the data into features and target
    features = data.drop('breed', axis=1)
    target = data['breed']

    # Convert categorical features into numerical values
    features_encoded = pd.get_dummies(features)

    # Train a Random Forest model
    model = RandomForestClassifier()
    model.fit(features_encoded, target)

    # Accept user input for the dog's features
    temperament = form_data['temperament']
    group = form_data['group']
    shedding_category = form_data['shedding']
    grooming_frequency_category = form_data['grooming']
    energy_level_category = form_data['energy']
    trainability_category = form_data['trainability']
    demeanor_category = form_data['demeanor']

    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'Temperament': [temperament],
        'Group': [group],
        'Shedding_Category': [shedding_category],
        'Grooming_Frequency_Category': [grooming_frequency_category],
        'Energy_Level_Category': [energy_level_category],
        'Trainability_Category': [trainability_category],
        'Demeanor_Category': [demeanor_category]
    })

    # Encode the user input
    input_encoded = pd.get_dummies(input_data)

    # Ensure input_encoded has the same columns as features_encoded
    input_encoded = input_encoded.reindex(
        columns=features_encoded.columns, fill_value=0)

    # Make a prediction
    prediction = model.predict(input_encoded)[0]

    return prediction
