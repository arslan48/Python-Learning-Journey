import pandas as pd

df = pd.read_csv("dirty_pokemon.csv")

print(df.isnull())

print(df.isnull().sum())

df = df.fillna({"Type": "Unknown"}) 
print(df)

# df = df.drop(columns=["Attack"])
# print(df)

df = df.drop(index=7)
print(df)

df = df.fillna({"HP":"Not found"})
print(df)

df["Type"] = df["Type"].replace({"Electric": "ELECTRIC",
                                  "Grass": "GRASS" })
print(df)
