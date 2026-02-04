import pandas as pd

# Read raw sales data
df = pd.read_csv("../data/raw_sales.csv", encoding="latin1")

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create time features
df["Month"] = df["Order Date"].dt.month
df["Year"] = df["Order Date"].dt.year

# Remove missing values
df = df.dropna()

# Save cleaned data
df.to_csv("../data/clean_sales_data.csv", index=False)

print("ETL Pipeline Completed Successfully")
