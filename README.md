🚗 BMW Global Sales Prediction Dashboard
<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg" width="130"/> </p> <h2 align="center"> Machine Learning Powered Automotive Sales Intelligence </h2> <p align="center"> A production-style Streamlit dashboard that predicts BMW vehicle sales using real market and product features. </p> <p align="center">








</p>
✨ Project Highlights

🚀 End-to-End Machine Learning Pipeline

🧠 Multiple Model Comparison

🎯 Best Model: Linear Regression (R² ≈ 0.74)

🎨 BMW-Styled Premium UI

⚡ Real-Time Prediction Engine

📦 Deployment-Ready Structure

<hr>
📊 Overview

This project predicts BMW vehicle units sold using business and market attributes including:

Price (USD)

Marketing Spend

Dealership Count

Competition Index

Vehicle Segment

Engine Type

Country & Model

The objective is to simulate how automotive companies can leverage machine learning to support pricing strategy, marketing planning, and sales forecasting.

<hr>
🧠 How It Works
1️⃣ Data Processing

Removed duplicates

Created datetime feature

Cleaned structured variables

One-hot encoded categorical features

Built deployment-ready dataset

2️⃣ Model Training

Models evaluated:

Linear Regression ✅ Best

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

Why Linear Regression?
The dataset shows strong linear relationships between business drivers and vehicle sales, resulting in the highest R² score.

3️⃣ Deployment

The best model is deployed into a BMW-themed Streamlit dashboard featuring:

Dynamic dropdown inputs

Smart model filtering

Premium UI styling

Instant prediction output

<hr>
🖥️ Dashboard Preview
<p align="center"> 👉 Add your Streamlit dashboard screenshot here for maximum impact </p>
<hr>
⚙️ Tech Stack
Layer	Technology
Programming	Python
Data Processing	Pandas, NumPy
Machine Learning	Scikit-learn
Deployment	Streamlit
Visualization	Plotly
Model Storage	Joblib
<hr>
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
<hr>
▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
<hr>
📈 Key Results

Achieved strong predictive performance with R² ≈ 0.74

Built a production-style interactive dashboard

Demonstrated real-world automotive analytics workflow

<hr>
🔮 Future Enhancements

KPI analytics panels

Cloud deployment (Streamlit Cloud / Render)

Advanced hyperparameter tuning

Real-time market data integration

<hr>
👨‍💻 Author

Farhan
Data Science & Machine Learning Enthusiast

<p align="center"> ⭐ If you find this project useful, consider starring the repository! </p>
