from sklearn.neighbors import KNeighborsClassifier

# Dataset: [Action, Comedy, Drama]
X = [
    [5, 3, 2],   # User A
    [4, 3, 2],   # User B
    [1, 5, 4]    # User C
]

# Labels (type of user taste)
y = ["Action Lover", "Action Lover", "Comedy Lover"]

# Create model
model = KNeighborsClassifier(n_neighbors=1)

# Train model
model.fit(X, y)

# New user data
new_user = [[5, 2, 2]]

# Predict
prediction = model.predict(new_user)

print("Predicted Preference:", prediction[0])