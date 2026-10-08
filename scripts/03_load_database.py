import pandas as pd
import sqlite3

# Load the cleaned dataset
df = pd.read_csv("data/superstore_clean.csv")

# Create/connect to SQLite database
conn = sqlite3.connect("retail_sales.db")

# Load the dataframe into a SQL table named orders
df.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded into SQLite successfully.")
print("Rows loaded:", len(df))

conn.close()