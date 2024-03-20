from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Query
query = "This is the second document."

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Transform the query
query_tfidf = tfidf_vectorizer.transform([query])

# Calculate cosine similarity between query and documents
cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

# Get document ranks based on cosine similarities
document_ranks = sorted(range(len(cosine_similarities)), key=lambda i: cosine_similarities[i], reverse=True)

# Print ranked documents
print("Ranked Documents:")
for rank, index in enumerate(document_ranks):
    print(f"Rank {rank + 1}: {documents[index]}")
