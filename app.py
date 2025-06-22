import streamlit as st
import numpy as np
import joblib

# Load saved model and label encoder
rf = joblib.load('random_forest_model.joblib')
le = joblib.load('label_encoder.joblib')

st.title("🏦  Loan Acceptance Predictor ")

st.write("Please fill in your details below:")

# Valid Python variable name for Pin-code
pin_code = st.selectbox(
    "Select Pin Code",
    options=[110001, 110003, 110004, 110011, 110014],
    format_func=lambda x: f"{x}"
)

age = st.number_input("Age (20 to 60)", min_value=20, max_value=60, value=30)
fam_members = st.number_input("Family Members (1 or more)", min_value=1, value=1)
education = st.selectbox(
    "Education", 
    options=[1, 2, 3], 
    format_func=lambda x: {1: 'Post Graduate', 2: 'Graduate', 3: 'Under Graduate'}.get(x)
)
t_experience = st.number_input("Total Experience (0 to 50 years)", min_value=0, max_value=50, value=5)
income = st.number_input("Income (Minimum 30000)", min_value=30000, value=50000)
mortgage = st.number_input("Mortgage Amount", min_value=0, value=0)
fixed_deposit = st.selectbox("Fixed Deposit", options=[0, 1], format_func=lambda x: {0: 'No', 1: 'Yes'}.get(x))
demat = st.selectbox("Demat Account", options=[0, 1], format_func=lambda x: {0: 'No', 1: 'Yes'}.get(x))
net_banking = st.selectbox("Net Banking", options=[0, 1], format_func=lambda x: {0: 'No', 1: 'Yes'}.get(x))

# Button for prediction
if st.button("Check"):
    # Ensure the feature order matches the model training
    user_input = np.array([[pin_code, age, fam_members, education, t_experience, income, mortgage,
                            fixed_deposit, demat, net_banking, ]])
    
    prediction_encoded = rf.predict(user_input)[0]
    prediction = le.inverse_transform([prediction_encoded])[0]

    if prediction.lower() == 'yes':
        st.success("✅ The applicant has accepted the loan offer.")
    else:
        st.error("❌ The applicant has Not accepted the loan offer.")
