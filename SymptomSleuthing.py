import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix\nimport streamlit as st\n\n# Load dataset\ndef load_data():\n    data = pd.read_csv('healthcare_data.csv')  # Replace with your dataset path\n    return data\n\n# Preprocess data\ndef preprocess_data(data):\n    data.fillna(0, inplace=True)  # Simple imputation\n    return data\n\n# Train model\ndef train_model(X_train, y_train):\n    model = RandomForestClassifier(n_estimators=100)\n    model.fit(X_train, y_train)\n    return model\n\n# Main function\ndef main():\n    st.title('Disease Prediction from Symptoms')\n    st.write('This application predicts diseases based on user input symptoms.')\n\n    # Load and preprocess data\n    data = load_data()\n    data = preprocess_data(data)\n\n    # User input for symptoms\n    symptoms = st.multiselect('Select symptoms:', data.columns[1:])  # Assuming first column is label\n    if symptoms:\n        user_input = np.zeros(len(data.columns) - 1)\n        for symptom in symptoms:\n            index = data.columns.get_loc(symptom) - 1  # Adjust for label column\n            user_input[index] = 1\n\n        # Prepare data for model\n        X = data.iloc[:, 1:].values\n        y = data.iloc[:, 0].values\n        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n        # Train model\n        model = train_model(X_train, y_train)\n\n        # Make predictions\n        prediction = model.predict(user_input.reshape(1, -1))\n        st.write('Predicted Disease:', prediction[0])\n\n        # Show model performance\n        y_pred = model.predict(X_test)\n        st.write('Model Performance:')\n        st.text(classification_report(y_test, y_pred))\n        st.text(confusion_matrix(y_test, y_pred))\n\n        # Visualize results\n        st.subheader('Confusion Matrix')\n        cm = confusion_matrix(y_test, y_pred)\n        plt.figure(figsize=(10, 7))\n        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)\n        plt.title('Confusion Matrix')\n        plt.colorbar()\n        tick_marks = np.arange(len(set(y)))\n        plt.xticks(tick_marks, set(y))\n        plt.yticks(tick_marks, set(y))\n        plt.ylabel('True label')\n        plt.xlabel('Predicted label')\n        st.pyplot(plt)\n\nif __name__ == '__main__':\n    main()\n