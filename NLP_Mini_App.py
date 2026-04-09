from collections import Counter
import string

text = "Machine learning is transforming the world with powerful AI applications."

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize
words = text.split()

# Remove stopwords
stopwords = ["is", "the", "with"]
filtered = [w for w in words if w not in stopwords]

# Count frequency
freq = Counter(filtered)

print("Keywords:", freq.most_common(3))