# 💸 Loan Acceptance Predictor  
**Predicting Customer Decisions with Data Science**

## 📌 Project Overview  
**Loan Acceptance Predictor** is an end-to-end machine learning solution that predicts whether a customer will accept a personal loan offer based on their profile. It integrates predictive modeling, data visualization, and a user-friendly web interface.

> **Objective:**  
> Predict if a customer has accepted the personal loan offered in the last campaign.

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

## 🛠️ Tools & Technologies Used  
- **Python** – Data processing and model development  
- **Pandas, NumPy** – Data manipulation and handling  
- **Seaborn, Matplotlib** – Exploratory Data Analysis (EDA) and visualization  
- **Scikit-learn** – Random Forest Classifier model  
- **LabelEncoder** – Categorical data encoding  
- **Joblib** – Model persistence (saving & loading)  
- **Streamlit** – Web app frontend for real-time predictions  
- **Tableau** – Interactive dashboards for data visualization  

## 🔍 Process Workflow  

### 1. Data Preparation
- Cleaned raw customer data  
- Handled missing values and outliers  

### 2. Exploratory Data Analysis (EDA)
- Visualized relationships between features and loan acceptance  

### 3. Model Building
- Used Random Forest Classifier  
- Evaluated performance metrics  
- Saved the trained model using `joblib`  

### 4. Web App Development
- Built using **Streamlit**  
- Allows users to input values and get instant predictions  

### 5. Dashboard Creation
- Created in **Tableau**  
- Dashboards show:
  - Loan acceptance by education and income  
  - Mortgage vs Acceptance  
  - Age, Area, and Income distribution  
  - Acceptance rate and digital behavior insights  

## 📊 Key Insights  
- 📉 **Loan acceptance rate:** Only **7.67%**  
- 🎓 **Post-graduates** show higher income and acceptance  
- 💰 Higher income → higher loan acceptance probability  
- 🏠 High mortgage → lower acceptance probability  
- 📍 Pincode **110004** has the highest acceptance rates  
- 🔑 **Income** is the most important predictive feature  

## 💡 Key Learnings  
- Cleaning and preparing real-world datasets  
- Performing EDA and visual storytelling  
- Building and evaluating ML models  
- Using `joblib` for model storage  
- Developing frontend using Streamlit  
- Creating Tableau dashboards  

## 🌐 Final Thoughts  
**Loan Acceptance Predictor** reflects the power of data science in solving real-world challenges. This project connected:
- Raw data ➡️ Clean insights  
- Machine learning ➡️ Real-time predictions  
- Dashboards ➡️ Strategic decision-making  

## 📁 Repository Structure  
LoanAcceptancePredictor/
├── 📂 backend/                         # Python files and datasets for model training
│   ├── Main.ipynb                     # Jupyter Notebook with full ML pipeline
│   ├── loan_dataset.xlsx              # Original dataset
│   ├── cleaned_loan_dataset.xlsx      # Cleaned and preprocessed data
│   ├── dashboard_dataset.xlsx         # Data prepared for Tableau dashboard
│   ├── label_encoder.joblib           # Saved LabelEncoder
│   └── random_forest_model.joblib     # Trained Random Forest model
│
├── 📂 frontend/                        # Streamlit app interface
│   ├── app.py                         # Main Streamlit app
│   ├── dashboard_dataset.xlsx         # Dataset used for UI/insights
│   ├── label_encoder.joblib           # Same encoder used by frontend
│   ├── random_forest_model.joblib     # Loaded model for predictions
│   └── 📂 .streamlit/                  # Streamlit configuration
│       └── config.toml                # Streamlit settings (e.g., page title)
│
├── README.md                          # Project documentation
└── .gitignore                         # Files/folders to ignore during version control



**How to run the project**
set the path - cd path\to\your\project\frontend
run - streamlit run app.py
click - http://localhost:8501
