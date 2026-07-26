import pandas as pd

# Create dataset
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Math": [85, 78, 92, 74, 88],
    "Science": [90, 82, 95, 70, 91],
    "English": [88, 79, 89, 76, 84]
}

# Load dataset
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# First five rows
print("\nFirst Five Rows:")
print(df.head())

# Last five rows
print("\nLast Five Rows:")
print(df.tail())

# Shape
print("\nShape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
df.info()

print("Dataset loaded successfully.")