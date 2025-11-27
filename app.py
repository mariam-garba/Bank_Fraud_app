import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("Bank_transaction_model.pkl")

st.title("Bank Transaction Fraud Detection App")

st.write("Enter transaction details below to predict if it is fraudulent.")

# --- User Input Fields ---
transaction_id = st.text_input("Transaction ID")
account_id = st.text_input("Account ID")
transaction_amount = st.number_input("Transaction Amount", min_value=0.0)
transaction_type = st.selectbox("Transaction Type", ["Transfer", "Withdrawal", "Deposit", "Payment"])
location = st.text_input("Location")
device_id = st.text_input("Device ID")
ip_address = st.text_input("IP Address")
merchant_id = st.text_input("Merchant ID")
channel = st.selectbox("Channel", ["ATM", "Online", "Branch", "POS"])
customer_age = st.number_input("Customer Age", min_value=1)
customer_occupation = st.text_input("Customer Occupation")
transaction_duration = st.number_input("Transaction Duration (seconds)", min_value=0.0)
login_attempts = st.number_input("Login Attempts", min_value=0)
account_balance = st.number_input("Account Balance", min_value=0.0)
previous_transaction_date = st.text_input("Previous Transaction Date")


# Prepare input as DataFrame
input_data = pd.DataFrame({
    "TransactionID": [transaction_id],
    "AccountID": [account_id],
    "TransactionAmount": [transaction_amount],
    "TransactionDate": ["2025-01-01"],   # Placeholder if needed
    "TransactionType": [transaction_type],
    "Location": [location],
    "DeviceID": [device_id],
    "IP Address": [ip_address],
    "MerchantID": [merchant_id],
    "Channel": [channel],
    "CustomerAge": [customer_age],
    "CustomerOccupation": [customer_occupation],
    "TransactionDuration": [transaction_duration],
    "LoginAttempts": [login_attempts],
    "AccountBalance": [account_balance],
    "PreviousTransactionDate": [previous_transaction_date]
})

# Button to predict
if st.button("Predict Fraud"):
    try:
        prediction = model.predict(input_data)[0]
        result = "⚠️ Fraudulent Transaction" if prediction == -1 else "✔️ Legitimate Transaction"
        st.subheader("Prediction Result:")
        st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")
