import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df)

group = df.groupby("Type")
print(group["Weight"].mean())

print(group["HP"].max())

print(df[df["Type"]== "Dragon"])
print(df[df["Generation"]==1]["Name"].count())
light_pokemon = df["Weight"].min()
print(df[df["Weight"]==light_pokemon])