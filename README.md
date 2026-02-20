🚗 BMW Global Sales Prediction Dashboard

A premium machine learning web application that predicts BMW vehicle sales using advanced regression models and a modern Streamlit dashboard.

Built using Python, Machine Learning, Linear Regression, and Streamlit with a clean and interactive BMW-styled interface.

🚀 Overview

This project predicts vehicle units sold based on business and market factors such as pricing, vehicle segment, engine type, dealership count, and competition index.

The application:

Takes vehicle configuration inputs

Processes data using a trained ML model

Predicts sales instantly

Displays results with a premium BMW-style interface

🧠 How It Works
1️⃣ Data Preprocessing

Removed duplicate records

Created datetime feature from year & month

Cleaned numerical columns

One-hot encoded categorical features

Prepared deployment-ready dataset

2️⃣ Model Training

Multiple regression models were tested:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

📊 Best Model: Linear Regression
✔ R² Score ≈ 0.74

3️⃣ Deployment

The trained model is deployed using Streamlit to create an interactive BMW-style dashboard.

Dashboard Features:

Dynamic dropdown inputs

Smart model filtering by segment

Premium UI with BMW branding

Real-time predictions

⚙️ Tech Stack

Python

Pandas & NumPy

Scikit-learn

Streamlit

Plotly

Joblib

📂 Project Structure
BMW-Sales-Prediction/
│
├── app.py
├── train_model.py
├── bmw_sales_model.pkl
├── model_columns.pkl
├── bmw_global_sales_cleaned.csv
├── requirements.txt
└── README.md
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
📈 Key Highlights

End-to-end ML pipeline

Clean BMW-themed dashboard

Smart UI interactions

Production-style deployment

🚀 Future Improvements

Add live analytics panels

Advanced ensemble tuning

Cloud deployment (Streamlit Cloud / Render)

BMW-style KPI widgets

👨‍💻 Author

Farhan
Data Science & Machine Learning Enthusiast
