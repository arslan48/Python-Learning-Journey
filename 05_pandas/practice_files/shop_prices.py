import pandas as pd
items = {
    "Apple": 50,
    "Mango": 120,
    "Grapes": 60,
    "Pear": 200,
    "Orange": 80
}

s = pd.Series(items)
fil=s[s>150]
print(fil)

mango = s.loc["Mango"]
print(f"Mangos\n {mango}")

first_item = s.iloc[0]
print(f"First item\n {first_item}")