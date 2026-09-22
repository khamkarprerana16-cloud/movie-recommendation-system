import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load cleaned dataset
data = pd.read_csv("clean_movies.csv")

# Load TF-IDF matrix
with open("tfidf_matrix.pkl", "rb") as file:
    tfidf_matrix = pickle.load(file)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

print("Cosine similarity calculation completed.")

print("\nSimilarity Matrix Shape:")
print(similarity_matrix.shape)

# Save similarity matrix
with open("similarity_matrix.pkl", "wb") as file:
    pickle.dump(similarity_matrix, file)

print("\nSimilarity matrix saved as similarity_matrix.pkl")


print("\nWhy cosine similarity is used:")
print("Cosine similarity checks how similar two movie text vectors are.")
print("It compares the direction of the vectors instead of just their size.")
