# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Placeholder: Load the dataset
# df = pd.read_csv("your_dataset.csv")  # Uncomment when dataset is available

# Sample dataframe (for now)
df = pd.DataFrame({
    "A": np.random.randint(1, 100, 50),
    "B": np.random.uniform(1, 50, 50),
    "C": np.random.choice(["Yes", "No"], 50),
    "D": np.random.randn(50)
})

# Basic information about the dataset
print("Dataset Overview:")
print(df.info())
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in dataset:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Visualizations
plt.figure(figsize=(12, 5))
sns.histplot(df["A"], bins=10, kde=True)
plt.title("Distribution of Column A")
plt.show()

sns.pairplot(df)
plt.show()

# Save the cleaned dataset (if needed)
# df.to_csv("cleaned_dataset.csv", index=False)  # Uncomment when dataset is available

print("EDA script executed successfully!")
