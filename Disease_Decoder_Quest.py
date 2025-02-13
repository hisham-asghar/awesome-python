import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix\nimport streamlit as st\n\n# Load dataset\ndata = pd.read_csv('healthcare_data.csv')  # Replace with your dataset\n\n# Display the dataset\nst.title('Disease Prediction from Symptoms')\nst.write(data.head())\n\n# User inputs for symptoms\nst.sidebar.header('User Input Symptoms')\nsymptom1 = st.sidebar.selectbox('Symptom 1', data['symptom1'].unique())\nsymptom2 = st.sidebar.selectbox('Symptom 2', data['symptom2'].unique())\nsymptom3 = st.sidebar.selectbox('Symptom 3', data['symptom3'].unique())\n\n# Prepare input for prediction\ninput_data = pd.DataFrame([[symptom1, symptom2, symptom3]], columns=['symptom1', 'symptom2', 'symptom3'])\n\n# Preprocess data\nX = data.drop('disease', axis=1)\nY = data['disease']\nX_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)\n\n# Train model\nmodel = RandomForestClassifier()\nmodel.fit(X_train, Y_train)\n\n# Make prediction\nif st.button('Predict Disease'):\n    prediction = model.predict(input_data)\n    st.write(f'Predicted Disease: {prediction[0]}')\n\n# Display model performance metrics\nif st.button('Show Model Performance'):\n    Y_pred = model.predict(X_test)\n    st.write('Confusion Matrix:')\n    st.write(confusion_matrix(Y_test, Y_pred))\n    st.write('Classification Report:')\n    st.write(classification_report(Y_test, Y_pred))\n\n# Visualize feature importance\nif st.button('Show Feature Importance'):\n    feature_importance = model.feature_importances_\n    features = X.columns\n    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})\n    importance_df = importance_df.sort_values(by='Importance', ascending=False)\n    plt.figure(figsize=(10,6))\n    plt.barh(importance_df['Feature'], importance_df['Importance'])\n    plt.xlabel('Importance')\n    plt.title('Feature Importance')\n    st.pyplot(plt)\n\n# Run the app\nif __name__ == '__main__':\n    st.run()