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
