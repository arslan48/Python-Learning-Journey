import pandas as pd

# Load the anime dataset
anime_df = pd.read_csv("anime_full.csv")

# Group anime by genre and compute average episodes per genre
genre_groups = anime_df.groupby("Genre")
average_episodes_by_genre = genre_groups["Episodes"].mean()
print("Average episodes per genre:")
print(average_episodes_by_genre)

# Find the genre with the lowest average episode count
genre_with_lowest_average_episodes = average_episodes_by_genre.idxmin()
print("Genre with lowest average episode count:", genre_with_lowest_average_episodes)

# Count unique studios for each genre
unique_studios_per_genre = genre_groups["Studio"].nunique()
print("Unique studios per genre:")
print(unique_studios_per_genre)

# Filter anime released after 2015 and calculate average studio ratings for those titles
recent_anime = anime_df[anime_df["Year"] > 2015]
studio_groups_recent = recent_anime.groupby("Studio")
average_rating_by_studio_recent = studio_groups_recent["Rating"].mean()
print("Average studio ratings for anime released after 2015:")
print(average_rating_by_studio_recent)

# Count anime titles by season
anime_count_by_season = anime_df.groupby("Season")["Title"].count()
print("Anime count by season:")
print(anime_count_by_season)