import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import streamlit as st

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('healthcare_data.csv')  # Replace with your dataset
    return data

# Preprocess the data
def preprocess_data(data):
    data.fillna(0, inplace=True)
    X = data.drop('disease', axis=1)
    y = data['disease']
    return X, y

# Train the model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model

# Main function for the Streamlit app
def main():
    st.title('Disease Prediction from Symptoms')
    st.write('This app predicts diseases based on symptoms using machine learning.')

    # Load and preprocess data
    data = load_data()
    X, y = preprocess_data(data)

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # User input for symptoms
    st.header('Input Symptoms')
    symptom1 = st.number_input('Symptom 1 Severity (0-10)', min_value=0, max_value=10)
    symptom2 = st.number_input('Symptom 2 Severity (0-10)', min_value=0, max_value=10)
    symptom3 = st.number_input('Symptom 3 Severity (0-10)', min_value=0, max_value=10)
    symptom4 = st.number_input('Symptom 4 Severity (0-10)', min_value=0, max_value=10)

    # Create input array
    input_data = np.array([[symptom1, symptom2, symptom3, symptom4]])

    # Predict disease
    if st.button('Predict Disease'):
        prediction = model.predict(input_data)
        st.write(f'Predicted Disease: {prediction[0]}')

    # Show model performance
    if st.button('Show Model Performance'):
        y_pred = model.predict(X_test)
        st.write('Classification Report:')
        st.text(classification_report(y_test, y_pred))
        st.write('Confusion Matrix:')
        st.text(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    main()