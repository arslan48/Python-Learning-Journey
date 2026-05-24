import pandas as pd

anime = pd.read_csv("anime.csv",index_col="AnimeTitle")

# Selection 

print("\n==Dataframe==")
print(anime)

print("\n==Title and Rating")
print(anime[["Rating"]])

print("\n==Rating above 9.0+==")
print(anime[anime["Rating"]>=9.0])

print("\n==Anime(s) with Most Episodes==")
max_eps = anime["Episodes"].max()
print(f"Most episodes: {max_eps}")
print(anime[anime["Episodes"] == max_eps])

print("\n==Anime made by MAPPA studio==")
print(anime[anime["Studio"]=="MAPPA"])

# Slicing

print("\n==Bleach==")
print(anime.loc["Bleach"])

print("\n Anime b/w Death Note and HXH")
print(anime.loc["Death Note": "Hunter x Hunter"])

# Specific anime + specific columns
print("\n==Bleach (Genre & Rating)==")
print(anime.loc["Bleach",["Rating","Studio"]])

# Search with error handling

anime_name = input("Enter the anime name: ")
try:
    print(anime.loc[anime_name])
except KeyError:
    print(f"{anime_name} not found")