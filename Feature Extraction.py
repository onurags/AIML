from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "Machine learning is fun",
    "Python is great for machine learning",
    "Feature extraction is an important step"
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names
features = vectorizer.get_feature_names_out()

# Convert to array for viewing
matrix_array = tfidf_matrix.toarray()

# Print features and matrix
print("Features:", features)
print("TF-IDF Matrix:\n", matrix_array)
