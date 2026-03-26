import pandas as pd

# Load dataset
df = pd.read_csv("sample_dataset.csv")

# Show top 5 rows
print("Top 5 Rows:")
print(df.head())

# Find highest average column
numeric = df.select_dtypes(include='number')

if len(numeric.columns) > 0:
    print("\nColumn with highest average:")
    print(numeric.mean().idxmax())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())