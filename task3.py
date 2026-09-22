import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# Load cleaned dataset
data = pd.read_csv("clean_movies.csv")

# Replace missing values with empty text
data["clean_text"] = data["clean_text"].fillna("")

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    max_features=3000,
    ngram_range=(1, 2)
)

# Convert text into vectors
tfidf_matrix = vectorizer.fit_transform(data["clean_text"])

print("TF-IDF vectorization completed.")

print("\nTF-IDF Matrix Shape:")
print(tfidf_matrix.shape)

# Save TF-IDF matrix
with open("tfidf_matrix.pkl", "wb") as file:
    pickle.dump(tfidf_matrix, file)

# Save vectorizer
with open("vectorizer.pkl", "wb") as file:
    pickle.dump(vectorizer, file)

print("\nTF-IDF matrix saved.")
print("Vectorizer saved.")
