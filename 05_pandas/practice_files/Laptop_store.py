import pandas as pd

data = {
    "Brand": ["Dell","HP","Lenovo","Asus","Acer"],
    "Price": [85000,95000,75000,110000,70000],
    "RAM": [8,16,8,32,4],
    "Storage": [256,512,256,1024,128]
}

df = pd.DataFrame(data, index=range(1,6))

df["Discount"] = [5000,3000,4000,2000,6000]
df["Discounted_price"] = df["Price"] - df["Discount"] 

print(df)

print("Prices")
print(df["Price"])

max_price = df["Price"].max()
print(df[df["Price"] == max_price])

print(df[df["RAM"]>= 16])

