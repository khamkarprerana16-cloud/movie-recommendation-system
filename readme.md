# Movie Recommendation System

## Assignment 20

This project is a simple content-based movie recommendation system.

It recommends movies that are similar to the movie selected by the user. The movie overview is used to find similar movies.

## Dataset

Dataset: TMDB 5000 Movie Dataset

Source: Kaggle

Kaggle Link:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Important columns used:

- `title` - Movie name
- `overview` - Movie description used for recommendation

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Git
- GitHub
- Render

## Tasks Completed

### Task 1 - Load and Understand Dataset
The dataset is loaded using Pandas. Dataset shape, column names, first five rows and missing values are checked.

### Task 2 - Text Preprocessing
The movie overview is cleaned by:

- Converting text to lowercase
- Removing special characters
- Removing some common stopwords
- Handling missing values

The cleaned text is stored in the `clean_text` column.

### Task 3 - TF-IDF Vectorization
TF-IDF is used to convert the movie descriptions into numerical vectors.

### Task 4 - Similarity Computation
Cosine similarity is used to find the similarity between movies.

### Task 5 - Recommendation Function
A recommendation function is created to find the top 5 movies similar to the selected movie.

### Task 6 - Streamlit Interface
A simple Streamlit interface is created where the user can select a movie and get recommendations.

### Task 7 - Git and GitHub
The project is uploaded to a GitHub repository using Git.

### Task 8 - Render Deployment
The Streamlit application is deployed using Render by connecting it with GitHub.

### Task 9 - Final Validation
The deployed application is tested to check whether the movie selection and recommendations are working correctly.

## How to Run the Project

First install the required libraries:

```bash
pip install -r requirements.txt