# Feature Extraction Example with Realistic Data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
import pandas as pd
from textblob import TextBlob
import string

# Sample realistic data: product reviews
reviews = [
    "I love this phone! The camera quality is amazing and battery lasts all day.",
    "Terrible customer service. I will not buy from this company again.",
    "The laptop is fast, lightweight, and has a beautiful display.",
    "Battery life is disappointing. It barely lasts 3 hours.",
    "Excellent headphones! Great sound quality and very comfortable.",
    "The screen cracked after a week. Not happy with the build quality.",
    "Superb performance and value for money. Highly recommend!",
    "The app crashes frequently and is full of bugs.",
    "Customer support was very helpful and resolved my issue quickly.",
    "The design is sleek and modern. Love the color options!"
]

# Add custom stopwords if needed
custom_stop_words = text.ENGLISH_STOP_WORDS.union(["phone", "laptop", "headphones", "app"])

# Create TF-IDF vectorizer with unigrams and bigrams, stopword removal, and lowercase conversion
vectorizer = TfidfVectorizer(stop_words=list(custom_stop_words), lowercase=True, ngram_range=(1,2))

# Fit and transform the reviews
tfidf_matrix = vectorizer.fit_transform(reviews)
features = vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=features)

# Additional features
length_features = []
for review in reviews:
    blob = TextBlob(review)
    words = review.split()
    num_chars = len(review)
    num_words = len(words)
    avg_word_len = sum(len(w) for w in words) / num_words if num_words > 0 else 0
    num_unique_words = len(set(words))
    num_stopwords = sum(1 for w in words if w.lower() in custom_stop_words)
    num_punct = sum(1 for c in review if c in string.punctuation)
    num_uppercase = sum(1 for w in words if w.isupper())
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    length_features.append({
        'num_chars': num_chars,
        'num_words': num_words,
        'avg_word_len': avg_word_len,
        'num_unique_words': num_unique_words,
        'num_stopwords': num_stopwords,
        'num_punct': num_punct,
        'num_uppercase': num_uppercase,
        'sentiment_polarity': sentiment_polarity,
        'sentiment_subjectivity': sentiment_subjectivity
    })
length_df = pd.DataFrame(length_features)

# Combine all features
total_features_df = pd.concat([length_df, tfidf_df], axis=1)

# Show a sample of the feature matrix
print("Feature columns:", total_features_df.columns.tolist())
print("\nFeature matrix (first 5 reviews):\n", total_features_df.head())
