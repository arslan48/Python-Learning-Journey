import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df)

group = df.groupby("Type")
print("\nAverage HP of all type of pokemon\n")
print(group["HP"].mean())

print("\nTotal pokemon in Type\n")
print(group["Name"].count())

print("\nMax Attack")
print(group["Attack"].max())

print("\nHighest average attack\n")
highest_avg_attack = df["Attack"].max()
print(df[df["Attack"] == highest_avg_attack][["Name","Attack"]])
print(highest_avg_attack)