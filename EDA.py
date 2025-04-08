import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Data Reference -> https://data.world/adsafj/coffee-shop/workspace/file?filename=Coffee+Chain.csv'''

# Load the dataset
df = pd.read_csv('Coffee_Chain.csv')

"""EDA"""
print(df.head())
print(df.info())

print("\nChecking for missing values...\n")
print(df.isnull().sum())

print("\nChecking for duplicates:\n", end=" ")
print(df.duplicated().sum())
print("\nSummarizing the data:\n")
print(df.describe())
print("\nColumns in the dataset:\n")
print(df.columns.tolist())

#Data Cleaning
# Convert columns to proper formats
df['Ddate'] = pd.to_datetime(df['Ddate'],format="%m/%d/%y")

# Remove commas and convert to numeric
df['Budget Sales'] = pd.to_numeric(df['Budget Sales'].str.replace(',', ''), errors='coerce')
df['Inventory'] = pd.to_numeric(df['Inventory'].str.replace(',', ''), errors='coerce')

# Drop redundant column if it's an exact copy
if 'Number Of Records' in df.columns and 'Number of Records' in df.columns:
    if df['Number of Records'].equals(df['Number Of Records']):
        df.drop('Number Of Records', axis=1, inplace=True)

# Rechecking the Data
print("Shape of dataset:", df.shape)
print("\nColumn Names:\n", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nDescriptive Statistics:\n", df.describe())

# 4. Unique Value Counts
category = df.select_dtypes(include='object').columns
for col in category:
    print(f"\nUnique values in '{col}': {df[col].nunique()}")


'''From here we will perform objectives'''


'''1st Market-Wise Performance Analysis'''


market_perf = df.groupby('Market')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False)
print("Market-wise performance:\n", market_perf)

# Reset index
market_perf_reset = market_perf.reset_index()

# Market-wise Coffee Sales Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(data=market_perf_reset, x='Market', y='Coffee Sales', hue='Market', palette='Blues_d', legend=False)
plt.title("Total Coffee Sales by Market")
plt.ylabel("Sales")
plt.xlabel("Market")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. State-wise aggregation
state_perf = df.groupby('State')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False)
print("State-wise performance:\n", state_perf.head(10))  # Top 10 states

# Reset index
top_states = state_perf.head(10).reset_index()

# Top 10 States Coffee Sales Bar Plot
plt.figure(figsize=(12, 6))
sns.barplot(data=top_states, x='State', y='Coffee Sales', hue='State', palette='Greens_d', legend=False)
plt.title("Top 10 States by Coffee Sales")
plt.ylabel("Sales")
plt.xlabel("State")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


'''2nd Product and Product Type Trends'''


# 1. Product Type Analysis
product_type_perf = df.groupby('Product Type')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False).reset_index()

plt.figure(figsize=(10, 5))
sns.barplot(data=product_type_perf, x='Product Type', y='Coffee Sales', hue='Product Type', palette='coolwarm', legend=False)
plt.title("Coffee Sales by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Total Coffee Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(data=product_type_perf, x='Product Type', y='Profit', hue='Product Type', palette='Pastel1', legend=False)
plt.title("Profit by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Sales vs Profit for Products
top_products = df.groupby('Product')[['Coffee Sales', 'Profit']].sum().sort_values(by='Coffee Sales', ascending=False).head(10).reset_index()
x = top_products['Coffee Sales']
y = top_products['Profit']
labels = top_products['Product']

plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(x, y, color='crimson', marker='o', s=100, label='Products')

# Add annotations for each point
for i in range(len(labels)):
    plt.text(x[i] + 100, y[i], labels[i], fontsize=10)

plt.title("Scatter Plot - Coffee Sales vs Profit (Top 10 Products)")
plt.xlabel("Coffee Sales")
plt.ylabel("Profit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
