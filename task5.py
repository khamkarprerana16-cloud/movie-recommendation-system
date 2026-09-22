import pandas as pd
import pickle

# Load dataset
data = pd.read_csv("clean_movies.csv")

# Load similarity matrix
with open("similarity_matrix.pkl", "rb") as file:
    similarity_matrix = pickle.load(file)


def recommend(item_name, top_n=5):

    # Find movie index
    movie_index = data[data["title"].str.lower() == item_name.lower()].index

    if len(movie_index) == 0:
        print("Movie not found.")
        return

    movie_index = movie_index[0]

    # Get similarity scores
    scores = list(enumerate(similarity_matrix[movie_index]))

    # Sort from highest to lowest
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommendations for:", data.iloc[movie_index]["title"])
    print()

    count = 0

    for index, score in scores:

        # Skip the selected movie
        if index == movie_index:
            continue

        print(data.iloc[index]["title"], "-", round(score, 2))

        count = count + 1

        if count == top_n:
            break


# Test with 3 different movies
recommend("Avatar")
recommend("The Dark Knight")
recommend("Titanic")
