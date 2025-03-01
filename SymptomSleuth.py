import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import streamlit as st

# Case Study: Predicting Diseases from Symptoms
st.title('Disease Prediction from Symptoms')
st.write('This interactive case study allows you to predict diseases based on symptoms using a Random Forest Classifier.')

# Load dataset
data = pd.read_csv('symptoms.csv')

# Display dataset
if st.checkbox('Show raw data'):
    st.write(data)

# Preprocessing
X = data.drop('Disease', axis=1)
y = data['Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Prediction
st.sidebar.header('Input Symptoms')
input_data = {}
for col in X.columns:
    input_data[col] = st.sidebar.slider(f'{col}', 0, 1, 0)

input_df = pd.DataFrame([input_data])
prediction = model.predict(input_df)

# Display Prediction
st.subheader('Prediction')
st.write(f'The predicted disease is: {prediction[0]}')

# Model Evaluation
st.subheader('Model Evaluation')
st.write('Accuracy on test set: {:.2f}%'.format(accuracy_score(y_test, model.predict(X_test)) * 100))

# Mini-Experiment
st.subheader('Mini-Experiment')
st.write('Adjust the number of trees in the forest and observe the change in accuracy.')
n_estimators = st.slider('Number of trees', 1, 200, 100)
model_experiment = RandomForestClassifier(n_estimators=n_estimators)
model_experiment.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model_experiment.predict(X_test))
st.write(f'Accuracy with {n_estimators} trees: {accuracy * 100:.2f}%')

# Visualization
st.subheader('Feature Importance')
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(10, 6))
plt.title('Feature Importances')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=90)
plt.xlabel('Relative Importance')
st.pyplot(plt)
