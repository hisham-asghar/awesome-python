import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report, confusion_matrix\nimport streamlit as st\n\n# Sample dataset for fraud detection\ndata = {'TransactionID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],\n        'Amount': [100, 1500, 200, 300, 2500, 600, 700, 800, 900, 10000],\n        'IsFraud': [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]}\ndf = pd.DataFrame(data)\n\n# Streamlit app setup\nst.title('Fraud Detection Case Study')\n\n# User input for tweaking parameters\namount_threshold = st.slider('Select Amount Threshold:', 100, 10000, 500)\n\n# Function to detect fraud based on amount threshold\ndef detect_fraud(df, threshold):\n    df['Predicted'] = np.where(df['Amount'] > threshold, 1, 0)\n    return df\n\n# Applying the fraud detection function\ndf = detect_fraud(df, amount_threshold)\n\n# Display the updated DataFrame\nst.write('Updated Transactions:', df)\n\n# Confusion matrix and classification report\nX = df[['Amount']]\nY = df['IsFraud']\nX_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)\n\nmodel = RandomForestClassifier()\nmodel.fit(X_train, Y_train)\nY_pred = model.predict(X_test)\n\n# Display results\nst.write('Classification Report:', classification_report(Y_test, Y_pred))\n\n# Plotting confusion matrix\ncm = confusion_matrix(Y_test, Y_pred)\nfig, ax = plt.subplots()\nax.matshow(cm, cmap=plt.cm.Blues)\nfor (i, j), val in np.ndenumerate(cm):\n    ax.text(j, i, val, ha='center', va='center')\nplt.xlabel('Predicted')\nplt.ylabel('True')\nplt.title('Confusion Matrix')\n\nst.pyplot(fig)\n\n# Conclusion and insights\nst.write('By adjusting the amount threshold, you can see how the model predicts fraud. Try different values to observe changes in the results!')