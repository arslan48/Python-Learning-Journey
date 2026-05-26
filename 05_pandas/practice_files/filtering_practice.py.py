import pandas as pd

df = pd.read_csv("products.csv")
print(df)

high_rated=df[df["Rating"]>= 9.0]
print("\nHigher rated products\n")
print(high_rated)

Laptop = df[df["Category"]== "Laptop"]
print("\nlaptop\n")
print(Laptop)

Apple = df[df["Brand"]== "Apple"]
print("\nApple Brand\n")
print(Apple)

price = df[df["Price"] < 100000]
print("\nCheap phones\n")
print(price)

Brand = df[(df["Brand"]=="Dell") | (df["Brand"]== "Sony")]
print("\n Sony or Dell")
print(Brand)

high_rated_laptops = df[(df["Rating"]>= 8.5) & (df["Category"]== "Laptop")]
print("\nHigh rated laptops\n")
print(high_rated_laptops)