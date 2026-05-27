import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df)

average_hp = df["HP"].mean()
print(average_hp)

highest_attack = df["Attack"].max()
print(highest_attack)

lowest_weight = df["Weight"].min()
print(lowest_weight)

fire_type_pokemon = df[df["Type"] == "Fire"]
print(fire_type_pokemon)

high_hp_pokemon = df[df["HP"] >= 90]
print(high_hp_pokemon)

print(df.count())

