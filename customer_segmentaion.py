import pandas as pd
from sklearn.cluster import KMeans

data = {
    "Income": [15, 20, 25, 30, 50, 55, 60, 65, 80, 85, 90, 95],
    "Spending": [20, 25, 30, 35, 60, 65, 70, 75, 40, 45, 50, 55]
}

df = pd.DataFrame(data)

X = df[["Income", "Spending"]]

kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

print(df)