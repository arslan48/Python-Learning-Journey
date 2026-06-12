import pandas as pd

# Load anime dataset
anime_df = pd.read_csv("anime_full.csv")

# Group anime data by Studio
studio_group = anime_df.groupby("Studio")

# Calculate average rating per studio
studio_avg_rating = studio_group["Rating"].mean()
print("Average Rating by Studio:")
print(studio_avg_rating)

# Find studio with highest average rating
highest_rating_studio = studio_avg_rating.idxmax()
print("\n--- Highest Rating Studio ---")
print(highest_rating_studio)

# Count anime titles per genre
genre_group = anime_df.groupby("Genre")
print("\n--- Anime Count by Genre ---")
print(genre_group["Title"].count())

# Find maximum episodes per studio
print("\n--- Maximum Episodes by Studio ---")
print(studio_group["Episodes"].max())

# Find maximum rating per studio
print("\n--- Maximum Rating by Studio ---")
print(studio_group["Rating"].max())
