from textblob import TextBlob

def analyze_sentiment(text):

    blob = TextBlob(text)

    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"

    elif polarity < 0:
        sentiment = "Negative 😞"

    else:
        sentiment = "Neutral 😐"

    return sentiment, polarity


print("===== Sentiment Analysis Tool =====")

user_text = input("Enter your text: ")

sentiment, polarity = analyze_sentiment(user_text)

print("\nResult")
print("-------------------")
print("Text      :", user_text)
print("Polarity  :", polarity)
print("Sentiment :", sentiment)