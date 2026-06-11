import pandas as pd

anime_df = pd.read_csv("anime_full.csv") 

mappa_studio = anime_df[anime_df["Studio"] == "MAPPA"]
print("\nMAPPA Studio")
print(mappa_studio)

high_rating = anime_df[anime_df["Rating"]>=9.0]

genre = anime_df[(anime_df["Genre"]=="Sci-Fi") | (anime_df["Genre"]=="Action")]

top_anime_after_2015 = anime_df[(anime_df["Year"] > 2015) & (anime_df["Rating"]>= 8.7)]

long_running_anime = anime_df[anime_df["Episodes"]> 100]
print("\n--- Long Running Anime (> 100 eps) ---")
print(long_running_anime)