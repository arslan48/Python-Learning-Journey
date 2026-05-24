import pandas as pd

df = pd.read_json("students.json").set_index("Name")

# Movies

movies = pd.read_json("Movies.json").set_index("Title")
print(movies)

# Selection by Column

print(movies[["Rating"]])
print(movies["Genre"])

# Selection by Row
print(movies)
print(movies.loc["The Dark Knight"])
