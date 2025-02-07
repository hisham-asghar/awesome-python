import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix\nimport streamlit as st\n\n# Load dataset\ndef load_data():\n    data = pd.read_csv('healthcare_data.csv')  # Placeholder for actual dataset\n    return data\n\n# Preprocess data\ndef preprocess_data(data):\n    # Example preprocessing steps\n    data = data.dropna()  # Remove missing values\n    X = data.drop('disease', axis=1)  # Features\n    y = data['disease']  # Target\n    return X, y\n\n# Train model\ndef train_model(X, y):\n    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n    model = RandomForestClassifier()\n    model.fit(X_train, y_train)\n    return model, X_test, y_test\n\n# Evaluate model\ndef evaluate_model(model, X_test, y_test):\n    predictions = model.predict(X_test)\n    report = classification_report(y_test, predictions)\n    cm = confusion_matrix(y_test, predictions)\n    return report, cm\n\n# Visualize results\ndef visualize_results(cm):\n    plt.figure(figsize=(10,7))\n    sns.heatmap(cm, annot=True, fmt='d')\n    plt.title('Confusion Matrix')\n    plt.xlabel('Predicted')\n    plt.ylabel('Actual')\n    plt.show()\n\n# Streamlit app\ndef main():\n    st.title('Disease Prediction from Symptoms')\n    st.write('This app predicts diseases based on symptoms using a Random Forest model.')\n\n    # Load and preprocess data\n    data = load_data()\n    X, y = preprocess_data(data)\n\n    # Train model\n    model, X_test, y_test = train_model(X, y)\n\n    # Evaluate model\n    report, cm = evaluate_model(model, X_test, y_test)\n    st.write('### Model Evaluation')\n    st.text(report)\n\n    # Visualize results\n    st.write('### Confusion Matrix')\n    visualize_results(cm)\n\n    # User input for prediction\n    st.write('### Predict Disease')\n    symptoms = st.text_input('Enter symptoms (comma separated):')\n    if symptoms:\n        input_data = np.array([symptoms.split(',')]).astype(float)  # Placeholder for actual input processing\n        prediction = model.predict(input_data)\n        st.write(f'Predicted Disease: {prediction[0]}')\n\nif __name__ == '__main__':\n    main()\n