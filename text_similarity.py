from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Take input from user
text = [
    input("Enter sentence 1: "),
    input("Enter sentence 2: ")
]

# Convert text to vectors
vectorizer = CountVectorizer().fit_transform(text)
vectors = vectorizer.toarray()

# Calculate similarity
similarity = cosine_similarity(vectors)

print("Similarity Score:", similarity[0][1])