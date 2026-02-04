import pandas as pd
from sklearn.linear_model import LinearRegression

# Load cleaned data
df = pd.read_csv("../data/clean_sales_data.csv")

# Monthly sales aggregation
monthly_sales = df.groupby(["Year", "Month"])["Sales"].sum().reset_index()

# Prepare features
X = monthly_sales[["Year", "Month"]]
y = monthly_sales["Sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict sales
monthly_sales["Predicted_Sales"] = model.predict(X)

# Save forecast
monthly_sales.to_csv("../data/sales_forecast.csv", index=False)

print("Sales Forecast Model Executed Successfully")
