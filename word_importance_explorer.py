from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Machine learning is very powerful",
    "AI and machine learning are related fields",
    "Natural language processing is part of AI",
    "Deep learning is a subset of machine learning",
    "AI is transforming the world"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

for i, doc in enumerate(X):
    print(f"\nDocument {i+1} Top Words:")
    sorted_items = sorted(zip(doc.toarray()[0], feature_names), reverse=True)
    for score, word in sorted_items[:3]:
        print(word, ":", round(score, 2))