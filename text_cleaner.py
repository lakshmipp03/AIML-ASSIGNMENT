import re

# Simple stopwords list
stopwords = ["is", "a", "the", "to", "in", "and", "of"]

def clean_text(text):
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stopwords]
    
    return " ".join(words)

# Test
sentence = "This is a Sample sentence, with punctuation!"
cleaned = clean_text(sentence)

print("Original:", sentence)
print("Cleaned:", cleaned)