
# 💸 Loan Acceptance Predictor  
**Predicting Customer Decisions with Data Science**

---


## 📌 Project Overview  
**Loan Acceptance Predictor** is an end-to-end machine learning solution that predicts whether a customer will accept a personal loan offer based on their profile. It integrates predictive modeling, data visualization, and a user-friendly Streamlit web interface.

> **Objective:** Predict if a customer accepted the personal loan offered in the last campaign.

---

## 🧠 Features Considered  
The model uses the following features:
- Age  
- Pincode  
- Work Experience  
- Income  
- Education  
- Number of Family Members  
- Net Banking  
- Fixed Deposit  
- Demat  
- Mortgage  

---

## 🛠️ Tools & Technologies Used  
- **Python** – Data processing and model development  
- **Pandas, NumPy** – Data manipulation and handling  
- **Seaborn, Matplotlib** – Exploratory Data Analysis (EDA) and visualization  
- **Scikit-learn** – Random Forest Classifier model  
- **LabelEncoder** – Categorical data encoding  
- **Joblib** – Model persistence (saving & loading)  
- **Streamlit** – Web app frontend for real-time predictions  
- **Tableau** – Interactive dashboards for data visualization  

---

## 📁 Repository Structure

```
LoanAcceptancePredictor/
├── 📂 backend/
│   ├── Main.ipynb
│   ├── loan_dataset.xlsx
│   ├── cleaned_loan_dataset.xlsx
│   ├── dashboard_dataset.xlsx
│   ├── label_encoder.joblib
│   └── random_forest_model.joblib
│
├── 📂 frontend/
│   ├── app.py
│   ├── dashboard_dataset.xlsx
│   ├── label_encoder.joblib
│   ├── random_forest_model.joblib
│   └── 📂 .streamlit/
│       └── config.toml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run This Project Locally

### ✅ Prerequisites:
- Python 3.8 or above installed
- Required packages installed (`streamlit`, `pandas`, `scikit-learn`, etc.)

### 💻 Steps:

1. **Open Command Prompt**

2. **Navigate to the frontend directory:**

```bash
cd path\to\your\project\frontend
```

3. **Run the Streamlit app:**

```bash
streamlit run app.py
```

4. **Click the link generated in the terminal**, usually:

```
http://localhost:8501
```

---

## 📊 Key Insights  
- Loan acceptance rate is only **7.67%**
- Post-graduates show higher income and loan acceptance rates
- Higher income increases likelihood of accepting a loan
- People with high mortgage tend to reject loans
- Pincode **110004** shows highest acceptance rate
- **Income** is the most important predictive feature

---

## 💡 Key Learnings  
- Data cleaning and preprocessing  
- Exploratory data analysis (EDA)  
- Model building and evaluation  
- Using `joblib` for model saving/loading  
- Web app deployment using Streamlit  
- Data storytelling through Tableau dashboards  

---

## 📌 Future Improvements  
- Add more features like credit score and loan type  
- Deploy the Streamlit app on cloud (Streamlit Cloud / Heroku)  
- Add SHAP for model explainability  
- Improve UI/UX design  

---

## 📬 Contact  
**Mangipudi Sanyasi Rao** – • [Email](sanyasiraomangipudi7@gmail.com)

---

> _"Data without insight is just noise. This project turns that noise into decision-making power."_
