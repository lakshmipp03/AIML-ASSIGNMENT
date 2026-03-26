import pandas as pd
from sklearn.cluster import KMeans

# Sample dataset (Annual Income, Spending Score)
data = {
    "Income": [15, 16, 17, 18, 50, 52, 54, 55, 80, 82, 85, 87],
    "Spending": [39, 40, 42, 43, 60, 61, 63, 65, 20, 22, 25, 27]
}

df = pd.DataFrame(data)

# Select features
X = df[["Income", "Spending"]]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

print(df)