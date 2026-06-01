import pandas as pd 

df = pd.read_csv("movies2025.csv")

df = df.fillna({"Title": "Unknown",
                 "Genre": "Unknown"})

df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
print(df)