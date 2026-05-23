import pandas as pd

df = pd.read_csv("students_150.csv",index_col="name")
anime = pd.read_csv("anime.csv",index_col="AnimeTitle")
print(anime)

# Selection 

print(anime.loc["One Piece":"Bleach",["Rating","Status"]])
