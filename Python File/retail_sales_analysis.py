"""A simple analysis of the retail sales dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Find the CSV file. It can be beside this script or in the Raw Data folder.
script_folder = Path(__file__).resolve().parent
csv_file = script_folder / "retail_sales_dataset.csv"

if not csv_file.exists():
    csv_file = script_folder.parent / "Raw Data" / "retail_sales_dataset.csv"

if not csv_file.exists():
    print("Could not find retail_sales_dataset.csv.")
    print("Put it beside this script or in the Raw Data folder.")
    raise SystemExit

# Make a folder for the charts and summary tables.
output_folder = script_folder / "analysis_output"
output_folder.mkdir(exist_ok=True)

# Read the data and convert the order date to a date value.
sales_data = pd.read_csv(csv_file)
sales_data["Order_Date"] = pd.to_datetime(sales_data["Order_Date"], errors="coerce")

# Show a quick look at the original data.
print("DATASET OVERVIEW")
print("Rows and columns:", sales_data.shape)
print("\nFirst five rows:")
print(sales_data.head())
print("\nMissing values in each column:")
print(sales_data.isnull().sum())
print("\nDuplicate rows:", sales_data.duplicated().sum())

# Remove duplicate rows and rows missing information needed for this analysis.
sales_data = sales_data.drop_duplicates()
sales_data = sales_data.dropna(subset=["Order_Date", "Sales", "Profit", "Quantity"])

# Add a month column so we can add up sales by month.
sales_data["Month"] = sales_data["Order_Date"].dt.strftime("%Y-%m")

# Calculate the main totals.
total_sales = sales_data["Sales"].sum()
total_profit = sales_data["Profit"].sum()
number_of_orders = sales_data["Order_ID"].nunique()
units_sold = sales_data["Quantity"].sum()

if number_of_orders > 0:
    average_order_value = total_sales / number_of_orders
else:
    average_order_value = 0

if total_sales > 0:
    profit_margin = total_profit / total_sales * 100
else:
    profit_margin = 0

print("\nKEY NUMBERS")
print(f"Total sales: ₹{total_sales:,.2f}")
print(f"Total profit: ₹{total_profit:,.2f}")
print(f"Number of orders: {number_of_orders}")
print(f"Units sold: {units_sold}")
print(f"Average order value: ₹{average_order_value:,.2f}")
print(f"Profit margin: {profit_margin:.2f}%")

# Add up sales for each month, category, region, product, and payment method.
monthly_sales = sales_data.groupby("Month")["Sales"].sum().reset_index()

category_sales = sales_data.groupby("Category")["Sales"].sum().reset_index()
category_sales = category_sales.sort_values("Sales", ascending=False)

region_sales = sales_data.groupby("Region")["Sales"].sum().reset_index()
region_sales = region_sales.sort_values("Sales", ascending=False)

product_sales = sales_data.groupby("Product")["Sales"].sum().reset_index()
product_sales = product_sales.sort_values("Sales", ascending=False)
top_products = product_sales.head(10)

payment_sales = sales_data.groupby("Payment_Method")["Sales"].sum().reset_index()
payment_sales = payment_sales.sort_values("Sales", ascending=False)

print("\nSALES BY CATEGORY")
print(category_sales.to_string(index=False))
print("\nSALES BY REGION")
print(region_sales.to_string(index=False))
print("\nTOP 10 PRODUCTS BY SALES")
print(top_products.to_string(index=False))
print("\nSALES BY PAYMENT METHOD")
print(payment_sales.to_string(index=False))

# Save the summary tables as CSV files.
monthly_sales.to_csv(output_folder / "monthly_sales.csv", index=False)
category_sales.to_csv(output_folder / "category_sales.csv", index=False)
region_sales.to_csv(output_folder / "region_sales.csv", index=False)
top_products.to_csv(output_folder / "top_10_products.csv", index=False)
payment_sales.to_csv(output_folder / "payment_sales.csv", index=False)

# Draw and save a chart of sales by month.
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales["Month"], monthly_sales["Sales"], marker="o")
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder / "monthly_sales.png")
plt.close()

# Draw and save a chart of sales by category.
plt.figure(figsize=(8, 5))
plt.bar(category_sales["Category"], category_sales["Sales"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig(output_folder / "sales_by_category.png")
plt.close()

# Print the best results from the summary tables.
if not category_sales.empty and not region_sales.empty and not top_products.empty:
    print("\nQUICK OBSERVATIONS")
    print("Top category by sales:", category_sales.iloc[0]["Category"])
    print("Top region by sales:", region_sales.iloc[0]["Region"])
    print("Top product by sales:", top_products.iloc[0]["Product"])
    best_month = monthly_sales.loc[monthly_sales["Sales"].idxmax(), "Month"]
    print("Top month by sales:", best_month)

print("\nAnalysis finished.")
print("Tables and charts are saved in:", output_folder)
  