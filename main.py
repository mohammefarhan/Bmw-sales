import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data
df = pd.read_csv("bmw_global_sales_dataset.csv")

# create date column if needed
df['date'] = pd.to_datetime(
    df['year'].astype(str) + "-" + df['month'].astype(str) + "-01"
)

# target + features
y = df['units_sold']
X = df.drop(columns=['units_sold','date'])

# encode categorical columns
X = pd.get_dummies(X, drop_first=True)

# save column names (VERY IMPORTANT for deployment)
joblib.dump(X.columns.tolist(), "model_columns.pkl")

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train best model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# save model
joblib.dump(model, "bmw_sales_model.pkl")

print("✅ Model saved successfully")