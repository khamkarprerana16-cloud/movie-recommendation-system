import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
data = pd.read_csv("clean_movies.csv")

# Create TF-IDF
vectorizer = TfidfVectorizer(
    max_features=3000,
    ngram_range=(1, 2)
)

data["clean_text"] = data["clean_text"].fillna("")
tfidf_matrix = vectorizer.fit_transform(data["clean_text"])

# Calculate similarity
similarity_matrix = cosine_similarity(tfidf_matrix)


# Recommendation function
def recommend(movie_name):

    movie_index = data[data["title"] == movie_name].index[0]

    scores = list(enumerate(similarity_matrix[movie_index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    count = 0

    for index, score in scores:

        if index == movie_index:
            continue

        recommendations.append(data.iloc[index]["title"])

        count = count + 1

        if count == 5:
            break

    return recommendations


# App title
st.title("Movie Recommendation System")

st.write("Select a movie and get similar movie recommendations.")


# Movie dropdown
movie_name = st.selectbox(
    "Select a movie:",
    data["title"].values
)


# Recommendation button
if st.button("Recommend Movies"):

    results = recommend(movie_name)

    st.subheader("Recommended Movies")

    for movie in results:
        st.write(movie)
