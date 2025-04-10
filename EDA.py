import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = pd.read_csv('Coffee_Chain.csv')

# Basic data overview
print(df.head())                  
print(df.info())                  
print(df.isnull().sum())          
print(df.duplicated().sum())      
print(df.describe())
print(df.columns.tolist())        

# Convert date column to datetime
df['Ddate'] = pd.to_datetime(df['Ddate'], format="%m/%d/%y")

# Clean numeric columns by removing commas
df['Budget Sales'] = pd.to_numeric(df['Budget Sales'].str.replace(',', ''), errors='coerce')
df['Inventory'] = pd.to_numeric(df['Inventory'].str.replace(',', ''), errors='coerce')

# Drop duplicate column if values are identical
if 'Number Of Records' in df.columns and 'Number of Records' in df.columns:
    if df['Number of Records'].equals(df['Number Of Records']):
        df.drop('Number Of Records', axis=1, inplace=True)



# ---------- Objective 1: Market-Wise and State-Wise Performance ----------

# Market-wise sales distribution (Pie Chart)
market_perf = df.groupby('Market')['Coffee Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 8))
plt.pie(market_perf, labels=market_perf.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("husl"))
plt.title("Market-Wise Coffee Sales Distribution")
plt.axis('equal')
plt.tight_layout()
plt.show()

# Top 10 states by sales (Bar Plot)
state_perf = df.groupby('State')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False).head(10).reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(data=state_perf, x='State', y='Coffee Sales', hue='State', palette='Greens_d', legend=False)
plt.title("Top 10 States by Coffee Sales")
plt.ylabel("Sales")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Objective 2: Product and Product Type Trends ----------

# Product type sales and profit (Side-by-side Bar Plots)
product_type_perf = df.groupby('Product Type')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False).reset_index()
top_products = df.groupby('Product')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False).head(10).reset_index()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.barplot(data=product_type_perf, x='Product Type', y='Coffee Sales', hue='Product Type', palette='coolwarm', legend=False)
plt.title("Coffee Sales by Product Type")
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
sns.barplot(data=product_type_perf, x='Product Type', y='Profit', hue='Product Type', palette='Pastel1', legend=False)
plt.title("Profit by Product Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales vs Profit for top 10 products (Line + Scatter plot)
x = top_products['Coffee Sales']
y = top_products['Profit']
labels = top_products['Product']
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='g', label='Line')
plt.scatter(x, y, color='crimson', s=100, alpha=0.8, label='Points')
for i in range(len(labels)):
    plt.text(x[i] + 50, y[i], labels[i], fontsize=9)
plt.title("Coffee Sales vs Profit (Top 10 Products)")
plt.xlabel("Coffee Sales")
plt.ylabel("Profit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Objective 3: Budgeted vs Actual Sales & COGS ----------

# Drop missing values for budget and actual columns
budget_actual_df = df.dropna(subset=['Budget Sales', 'Coffee Sales', 'Budget Cogs', 'Cogs'])

# Compare Budget vs Actual Sales over time (Line Plot)
sales_comparison = budget_actual_df[['Ddate', 'Budget Sales', 'Coffee Sales']].groupby('Ddate').sum().reset_index()
plt.figure(figsize=(12, 5))
plt.plot(sales_comparison['Ddate'], sales_comparison['Budget Sales'], label='Budget Sales', linestyle='--', color='blue')
plt.plot(sales_comparison['Ddate'], sales_comparison['Coffee Sales'], label='Actual Sales', linestyle='-', color='green')
plt.title("Budgeted vs Actual Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Compare Budget vs Actual COGS over time (Line Plot)
cogs_comparison = budget_actual_df[['Ddate', 'Budget Cogs', 'Cogs']].groupby('Ddate').sum().reset_index()
plt.figure(figsize=(12, 5))
plt.plot(cogs_comparison['Ddate'], cogs_comparison['Budget Cogs'], label='Budget Cogs', linestyle='--', color='red')
plt.plot(cogs_comparison['Ddate'], cogs_comparison['Cogs'], label='Actual Cogs', linestyle='-', color='purple')
plt.title("Budgeted vs Actual Cost of Goods Sold Over Time")
plt.xlabel("Date")
plt.ylabel("COGS")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------- Objective 4: Time Series Analysis of Sales & Profit ----------

# Line plot for coffee sales over time
sales_over_time = df.groupby('Ddate')['Coffee Sales'].sum()
plt.figure(figsize=(12, 5))
plt.plot(sales_over_time.index, sales_over_time.values, marker='o', linestyle='-', color='blue')
plt.title("Line Plot - Total Coffee Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

# Line plot for profit over time
profit_over_time = df.groupby('Ddate')['Profit'].sum()
plt.figure(figsize=(12, 5))
plt.plot(profit_over_time.index, profit_over_time.values, marker='o', linestyle='-', color='purple')
plt.title("Line Plot - Total Profit Over Time")
plt.xlabel("Date")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

# Monthly sales using bar plot
monthly_sales = df.copy()
monthly_sales['Month'] = df['Ddate'].dt.to_period('M')
monthly_sales = monthly_sales.groupby('Month')['Coffee Sales'].sum().reset_index()
monthly_sales['Month'] = monthly_sales['Month'].dt.to_timestamp()

plt.figure(figsize=(12, 5))
sns.barplot(data=monthly_sales, x='Month', y='Coffee Sales', color='teal')
plt.title("Bar Plot - Monthly Coffee Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Objective 5: Marketing Impact Analysis ----------

# Scatter plots of marketing spend vs sales and profit
marketing_data = df[['Marketing', 'Coffee Sales', 'Profit']].dropna()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(marketing_data['Marketing'], marketing_data['Coffee Sales'], color='teal', alpha=0.6)
plt.title("Marketing Spend vs Coffee Sales")
plt.xlabel("Marketing Spend")
plt.ylabel("Coffee Sales")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(marketing_data['Marketing'], marketing_data['Profit'], color='tomato', alpha=0.6)
plt.title("Marketing Spend vs Profit")
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

# Heatmap showing correlations between numerical features
plt.figure(figsize=(10, 6))
corr_matrix = df[['Marketing', 'Coffee Sales', 'Profit', 'Cogs', 'Budget Sales', 'Budget Cogs']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap - Marketing vs Sales, Profit, and COGS")
plt.tight_layout()
plt.show()
