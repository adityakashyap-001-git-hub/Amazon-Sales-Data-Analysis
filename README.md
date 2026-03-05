# Amazon-Sales-Data-Analysis
📌 Project Overview

This project analyzes Amazon sales transactions from **January to April 2025** to understand revenue trends, product performance, and regional sales patterns using **Python, SQL, and Power BI**.

---

# 📁 Dataset Information

Columns included:

* Order ID
* Product Category
* Product
* Sales
* Profit
* Customer Location
* Payment Method
* Order Status
* Date

Total Records: **250+ transactions**

---

# 🛠 Tools & Technologies

* Python (Pandas, NumPy)
* SQL
* Power BI
* Excel

---

# 🧹 Data Cleaning (Python)

Steps performed:

• Removed null values
• Removed duplicate records
• Converted date column to datetime format
• Extracted **Month and Quarter**

Example Python code:

```python
import pandas as pd

df = pd.read_csv("amazon_sales.csv")

df.drop_duplicates(inplace=True)

df.isnull().sum()

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter
```

---

# 📊 Data Analysis (Python)

### Category-wise Revenue

```python
df.groupby('Product Category')['Sales'].sum()
```

### Product-wise Profit

```python
df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
```

### Orders by Location

```python
df['Customer Location'].value_counts()
```

---

# 🗄 SQL Queries Used

### Total Revenue

```sql
SELECT SUM(Sales) AS Total_Revenue
FROM amazon_sales;
```

### Revenue by Category

```sql
SELECT Product_Category,
SUM(Sales) AS Revenue
FROM amazon_sales
GROUP BY Product_Category
ORDER BY Revenue DESC;
```

### Profit by Product

```sql
SELECT Product,
SUM(Profit) AS Total_Profit
FROM amazon_sales
GROUP BY Product
ORDER BY Total_Profit DESC;
```

### Orders by Location

```sql
SELECT Customer_Location,
COUNT(Order_ID) AS Total_Orders
FROM amazon_sales
GROUP BY Customer_Location
ORDER BY Total_Orders DESC;
```

---

# 📈 Power BI Dashboard

### KPIs

* Total Revenue → **243.85K**
* Total Orders → **250**
* Total Profit → **73.15K**
* Avg Order Value → **975.38**
* Completion Rate → **92%**

---

# 📊 Visualizations Used

• KPI Cards – Revenue, Profit, Orders
• Bar Chart – Revenue by Category
• Bar Chart – Profit by Product
• Pie Chart – Order Status Distribution
• Map Visualization – Sales by Region
• Table – Product Performance
• Slicers – Category, Location, Payment Method

---

# 📌 Key Insights

1️⃣ **Electronics & Home Appliances generate more than 95% of revenue.**

2️⃣ **Refrigerator, Laptop and Smartphone are top profitable products.**

3️⃣ Sales demand is highest in **Houston and Miami**.

4️⃣ **Cancellation rate is around 7%**, indicating potential operational issues.

5️⃣ Categories like **Clothing and Books have low profit margins**.

---

# 📷 Dashboard Preview

Amazon Sales Dashboard (Power BI)

![IMG-20250530-WA0006(1) jpg](https://github.com/user-attachments/assets/2f5a4fac-9ce8-4e18-93cf-3d003a42f4ac)

---

# 3️⃣ Power BI DAX Measures

### Total Revenue

```DAX
Total Revenue = SUM(Sales[Total_Sales])
```

### Total Profit

```DAX
Total Profit = SUM(Sales[Profit])
```

### Average Order Value

```DAX
Avg Order Value =
DIVIDE([Total Revenue], [Total Orders])
```

### Profit Margin

```DAX
Profit Margin % =
DIVIDE([Total Profit], [Total Revenue])
```

### Orders YTD

```DAX
Orders YTD =
TOTALYTD([Total Orders], 'Date'[Date])
```

---




