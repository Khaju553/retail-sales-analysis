import sqlite3

conn = sqlite3.connect("retail_sales.db")
cursor = conn.cursor()

query = """
SELECT
    order_year,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM orders
GROUP BY order_year
ORDER BY order_year;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Yearly Sales and Profit Trend")
print("-----------------------------")

for row in results:
    print(row)

conn.close()