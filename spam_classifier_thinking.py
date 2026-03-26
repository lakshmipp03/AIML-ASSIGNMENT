import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample dataset
data = {
    "Message": [
        "Win a free iPhone",
        "Hello how are you",
        "Free entry in contest",
        "Let's meet tomorrow",
        "Claim your prize now"
    ],
    "Label": ["Spam", "Ham", "Spam", "Ham", "Spam"]
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["Message"])

# Labels
y = df["Label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Test with new message
new_msg = ["Free prize waiting for you"]
new_X = vectorizer.transform(new_msg)

prediction = model.predict(new_X)

print("Message:", new_msg[0])
print("Prediction:", prediction[0])