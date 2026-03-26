import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Area": [500, 800, 1000, 1200, 1500],
    "Price": [1000000, 1500000, 2000000, 2500000, 3000000]
}

df = pd.DataFrame(data)

# Feature and Label
X = df[["Area"]]
y = df["Price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict for new input
new_area = [[1300]]
predicted_price = model.predict(new_area)

print("Predicted price for 1300 sq.ft:", predicted_price[0])