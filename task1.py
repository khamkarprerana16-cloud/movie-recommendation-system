import pandas as pd

# Load dataset
data = pd.read_csv("tmdb_5000_movies.csv")

print("Dataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nFirst 5 Rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nText column used for recommendation:")
print("overview")
