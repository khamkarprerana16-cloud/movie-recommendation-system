import pandas as pd
import re

# Load dataset
data = pd.read_csv("tmdb_5000_movies.csv")

# Replace missing overview with empty string
data["overview"] = data["overview"].fillna("")

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z ]", "", text)

    words = text.split()

    stop_words = {
        "the", "is", "a", "an", "and", "or", "of",
        "to", "in", "on", "for", "with", "as", "by",
        "at", "from", "this", "that", "it", "be"
    }

    new_words = []

    for word in words:
        if word not in stop_words:
            new_words.append(word)

    return " ".join(new_words)


# Apply cleaning
data["clean_text"] = data["overview"].apply(clean_text)

# Save the cleaned data
data.to_csv("clean_movies.csv", index=False)

print("Text preprocessing completed.")

print("\nOriginal Text:")
print(data["overview"].iloc[0])

print("\nCleaned Text:")
print(data["clean_text"].iloc[0])

print("\nCleaned file saved as clean_movies.csv")
