import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix\nimport streamlit as st\n\n# Load dataset\ndef load_data():\n    # Simulating a dataset for fraud detection\n    data = {\n        'TransactionID': range(1, 101),\n        'Amount': np.random.randint(1, 1000, size=100),\n        'IsFraud': np.random.choice([0, 1], size=100, p=[0.9, 0.1])\n    }\n    return pd.DataFrame(data)\n\n# Function to train the model\ndef train_model(df):\n    X = df[['Amount']]\n    y = df['IsFraud']\n    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n    model = RandomForestClassifier()\n    model.fit(X_train, y_train)\n    return model, X_test, y_test\n\n# Function to display results\ndef display_results(y_test, y_pred):\n    st.subheader('Confusion Matrix')\n    cm = confusion_matrix(y_test, y_pred)\n    st.write(cm)\n    st.subheader('Classification Report')\n    report = classification_report(y_test, y_pred, output_dict=True)\n    st.write(report)\n    st.bar_chart(report['1'])\n\n# Streamlit app\ndef main():\n    st.title('Fraud Detection Case Study')\n    st.write('In this case study, we will detect fraudulent transactions based on transaction amount.')\n    df = load_data()\n    st.write('Dataset Preview:', df.head())\n    st.write('Adjust the parameters below to see how they affect the model.')\n    amount_threshold = st.slider('Transaction Amount Threshold', 1, 1000, 500)\n    df_filtered = df[df['Amount'] > amount_threshold]\n    st.write('Filtered Dataset:', df_filtered)\n    if st.button('Train Model'):\n        model, X_test, y_test = train_model(df_filtered)\n        y_pred = model.predict(X_test)\n        display_results(y_test, y_pred)\n\nif __name__ == '__main__':\n    main()