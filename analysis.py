import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/Superstore_Cleaned.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Correlation analysis
print("\nCorrelation Matrix:")
print(df[["Sales", "Quantity", "Discount", "Profit"]].corr())

# Outlier analysis using IQR
print("\nOutlier Counts:")
for column in ["Sales", "Quantity", "Discount", "Profit"]:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = ((df[column] < lower) | (df[column] > upper)).sum()
    print(column, ":", outliers)

# Sales and Profit by Category
print("\nSales and Profit by Category:")
print(df.groupby("Category")[["Sales", "Profit"]].sum().round(2))

# Sales and Profit by Region
print("\nSales and Profit by Region:")
print(df.groupby("Region")[["Sales", "Profit"]].sum().round(2))

# Sales and Profit by Sub-Category
print("\nSales and Profit by Sub-Category:")
print(
    df.groupby("Sub-Category")[["Sales", "Profit"]]
    .sum()
    .round(2)
    .sort_values("Sales", ascending=False)
)

# Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")

print("\nMonthly Sales Trend:")
print(df.groupby("Month")["Sales"].sum().round(2))

# Top 10 Customers
print("\nTop 10 Customers by Sales:")
print(
    df.groupby("Customer Name")["Sales"]
    .sum()
    .round(2)
    .sort_values(ascending=False)
    .head(10)
)

# Chart 1: Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/Sales_by_Category.png")
plt.close()

print("\nChart 1 saved successfully!")
# Chart 2: Profit by Category
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure()
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("visualizations/Profit_by_Category.png")
plt.close()

print("Chart 2 saved successfully!")
# Chart 3: Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualizations/Sales_by_Region.png")
plt.close()

print("Chart 3 saved successfully!")
# Chart 4: Sales by Sub-Category
subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
subcategory_sales.plot(kind="bar")
plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/Sales_by_SubCategory.png")
plt.close()

print("Chart 4 saved successfully!")
# Chart 5: Monthly Sales Trend
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/Monthly_Sales_Trend.png")
plt.close()

print("Chart 5 saved successfully!")
