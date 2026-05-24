import pandas as pd

df = pd.read_csv("students_150.csv",index_col="name")
anime = pd.read_csv("anime.csv")


# Selection 

print("\n==Dataframe==")
print(anime)

print("\n==Title and Rating")
print(anime[["AnimeTitle","Rating"]])

print("\n==Rating above 9.0+==")
print(anime[anime["Rating"]>=9.0])

print("\n==Anime(s) with Most Episodes==")
max_eps = anime["Episodes"].max()
print(f"Most episodes: {max_eps}")
print(anime[anime["Episodes"] == max_eps])

print("\n==Anime made by MAPPA studio==")
print(anime[anime["Studio"]=="MAPPA"])