
Loan Acceptance Predictor
- Predicting Customer Decisions with Data ScienceI built a project titled “Loan Acceptance Predictor”—a complete end-to-end solution designedto predict whether a customer will accept a personal loan offer based on their profile.
Overview
The objective of this project was to predict:
“Did this customer accept the personal loan offered in the last campaign?”
To solve this, I developed a machine learning model that takes inputs of customer details suchas:
* Age
* Pincode
* Work Experience
* Income
* Education
* Number of Family Members
* Net Banking
* Fixed Deposit
* Demat
* Mortgage
and predicts whether the customer is likely to accept the loan or not.
Tools & Technologies Used
This project helped me to explore multiple tools and skills , the following are :
Python Language: For data manipulation and model building
Pandas, Numpy : For data handling
Seaborn, Matplotlib : For exploratory data analysis (EDA) and data visualizationScikit-learn : For building and training the Random Forest classification model
LabelEncoder : For data preprocessing
Joblib : For saving and loading the trained machine learning model efficiently.
Streamlit : For the frontend of the model which will act as user interfaceFor dashboardTableau : To build interactive dashboards for visual storytelling . The dashboard containsmultiple charts and graphs which I have learned for this project .
From Raw Data to Predictive Model
Starting with raw customer data, I cleaned and processed the dataset, handled missing values,and dealed with outliers . Using EDA techniques , I visualized trends and correlations thatcould influence a customer's likelihood of accepting a loan.
I then trained a Random Forest Classifier, evaluated its performance, and usedjoblibto savethe trained model for reuse in the Streamlit web app—allowing real-time predictions withoutretraining every time.
Dashboards
With Tableau , I created an intuitive and interactive dashboard to visualize insights from thedata. This dashboard showcases trends such as income levels, digital behavior, and fixeddeposits in relation to loan acceptance , Loan acceptance by education levels , Income vsMortgage , Acceptance rate , Age distribution , Average income based on Education ,
Distribution over Area .
Streamlit App for Frontend
I developed a Streamlit web application that allows users to input data such as age, income,and digital usage—and instantly receive a prediction about loan acceptance. The model wasloaded using joblib, making the prediction process efficient and seamless.
My insights
“Loan Acceptance rate is only 7.67%, indicating very less chances of loan acceptancy.”“Post-graduates have higher average income and loan acceptance Rate.”
“Higher the income , higher chances of accepting the loan.”
“People with high income and low mortgage accepts the loan , where people with mortgagehave very low chances of accepting loan.”
“Feature importance of the dataset is Income , accepting the loan depends upon the income.”“Under-graduates have highest Avg Income.”
“Most People from Pin-code 110004 have Accepted the Personal Loan.”
“Higher the Mortgage , Low chances of Accepting the loan.”
Key Learnings
This project taught me a lot of valuable concepts and practical skills:
 How to clean and prepare real-world datasets
 Exploratory data analysis and visualization
 Building and tuning machine learning models
 Using `joblib` to save and load models
 Creating interactive dashboards
 Deploying a web app using Streamlit
Final Thoughts
One of the most exciting aspects of this project was seeing how everything connects—fromraw data to a well -established dashboard and predictive web app. The waydatavisualizations and real-time predictions bring a complete analysis of a dataset. “Loan Acceptance Predictor” is not just a project—it’s a reflection of how data science cansolve real-world problems through thoughtful analysis , dashboards and machine learningmodels .