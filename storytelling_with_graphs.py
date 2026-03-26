import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sample_dataset.csv")

# ---- Bar Chart ----
df["Name"].value_counts().plot(kind="bar")
plt.title("Count of Names")
plt.xlabel("Name")
plt.ylabel("Frequency")
plt.show()

# ---- Pie Chart ----
df["Name"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Name Distribution")
plt.ylabel("")
plt.show()

# ---- Histogram ----
df["Marks"].plot(kind="hist")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.show()