import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df)

group = df.groupby("Type")
print(group["Attack"].mean())
