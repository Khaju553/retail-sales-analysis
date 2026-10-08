import pandas as pd

df = pd.read_csv("data/superstore_raw.csv", encoding="latin-1")

print("Original shape:", df.shape)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUpdated data types:")
print(df[["Order Date", "Ship Date"]].dtypes)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("\nCleaned column names:")
print(df.columns.tolist())

# Check numeric columns for unusual values
print("\nNumeric column summary:")
print(df[["sales", "quantity", "discount", "profit"]].describe())

print("\nRows with negative sales:")
print((df["sales"] < 0).sum())

print("\nRows with zero or negative quantity:")
print((df["quantity"] <= 0).sum())

print("\nRows with discount below 0 or above 1:")
print(((df["discount"] < 0) | (df["discount"] > 1)).sum())

print("\nLoss-making rows:")
print((df["profit"] < 0).sum())

# Create useful derived columns
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month_name()
df["shipping_days"] = (df["ship_date"] - df["order_date"]).dt.days

# Profit margin percentage
df["profit_margin"] = (df["profit"] / df["sales"]) * 100

print("\nNew columns created:")
print(
    df[
        [
            "order_date",
            "order_year",
            "order_month",
            "shipping_days",
            "sales",
            "profit",
            "profit_margin",
        ]
    ].head()
)

# Save cleaned dataset
df.to_csv("data/superstore_clean.csv", index=False)

print("\nCleaned dataset saved successfully.")
print("Final shape:", df.shape)