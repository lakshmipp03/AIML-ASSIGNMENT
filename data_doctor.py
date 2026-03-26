import pandas as pd

# Load dataset
df = pd.read_csv("sample_dataset.csv")

print("Original Data:\n")
print(df)

# 1. Handle missing values
df = df.fillna("Unknown")

# 2. Remove duplicates
df = df.drop_duplicates()

# 3. Standardize text (convert to lowercase)
df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

print("\nCleaned Data:\n")
print(df)