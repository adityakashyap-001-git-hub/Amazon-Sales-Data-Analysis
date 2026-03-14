
# Amazon Sales Data Analysis
# Author: Aditya Kashyap
# Description: Data cleaning and analysis for Amazon sales dataset (Jan–Apr 2025)

import pandas as pd
import numpy as np

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("amazon_sales.csv")

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Check null values
print("Null Values in Dataset:")
print(df.isnull().sum())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month and Quarter
df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter

print("\nData after cleaning:")
print(df.head())

# -----------------------------
# Data Analysis
# -----------------------------

# Category-wise Revenue
category_revenue = df.groupby('Product Category')['Sales'].sum()
print("\nCategory-wise Revenue:")
print(category_revenue)

# Product-wise Profit
product_profit = df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
print("\nProduct-wise Profit:")
print(product_profit)

# Orders by Customer Location
orders_by_location = df['Customer Location'].value_counts()
print("\nOrders by Location:")
print(orders_by_location)

# -----------------------------
# Additional Useful Metrics
# -----------------------------

# Total Revenue
total_revenue = df['Sales'].sum()

# Total Profit
total_profit = df['Profit'].sum()

# Total Orders
total_orders = df['Order ID'].nunique()

# Average Order Value
avg_order_value = total_revenue / total_orders

print("\nKey Metrics")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", avg_order_value)

# -----------------------------
# Save cleaned dataset (optional)
# -----------------------------

df.to_csv("cleaned_amazon_sales.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_amazon_sales.csv'")
