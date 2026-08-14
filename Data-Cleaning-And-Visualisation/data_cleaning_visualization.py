import pandas as pd

df = pd.read_csv("sales_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())
print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])
# Fill missing Customer_City with the most common city
df["Customer_City"] = df["Customer_City"].fillna(df["Customer_City"].mode()[0])

# Fill missing Rating with the average rating
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Fill missing Customer_City with the most common city
df["Customer_City"] = df["Customer_City"].fillna(df["Customer_City"].mode()[0])

# Fill missing Rating with the average rating
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicates after cleaning
print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\nUnique Cities Before Cleaning:")
print(df["Customer_City"].unique())

# Standardize city names
df["Customer_City"] = df["Customer_City"].str.title()

# Check cities after cleaning
print("\nUnique Cities After Cleaning:")
print(df["Customer_City"].unique())

print("\nPrice Statistics:")
print(df["Price"].describe())

# Detect outliers using IQR method
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = df[(df["Price"] < lower_bound) | (df["Price"] > upper_bound)]

print("\nOutliers:")
print(outliers)

# Correct the erroneous laptop price
df.loc[df["Order_ID"] == 1024, "Price"] = 59000

print("\nPrice after correcting the outlier:")
print(df.loc[df["Order_ID"] == 1024])

print("\nFINAL DATA CHECK")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Cities:")
print(df["Customer_City"].unique())

print("\nNumber of Rows and Columns:")
print(df.shape)

import matplotlib.pyplot as plt

# Sales quantity by product
product_sales = df.groupby("Product")["Quantity"].sum()

plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")

plt.title("Total Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("product_sales.png")
plt.show()

# Calculate revenue
df["Revenue"] = df["Quantity"] * df["Price"]

# Total revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("product_revenue.png")
plt.show()

# Total quantity sold by city
city_sales = df.groupby("Customer_City")["Quantity"].sum()

plt.figure(figsize=(8, 5))
city_sales.plot(kind="bar")

plt.title("Total Quantity Sold by City")
plt.xlabel("Customer City")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("city_sales.png")
plt.show()

# Distribution of customer ratings
plt.figure(figsize=(8, 5))

plt.hist(df["Rating"], bins=[2.5, 3.5, 4.5, 5.5], edgecolor="black")

plt.title("Distribution of Customer Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Orders")

plt.xticks([3, 4, 5])

plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

import seaborn as sns

# Correlation between numerical variables
correlation = df[["Quantity", "Price", "Rating", "Revenue"]].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.show()