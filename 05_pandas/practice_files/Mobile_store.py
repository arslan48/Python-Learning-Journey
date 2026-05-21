import pandas as pd

data = {
    "Brand": ["Samsung","Apple","Oppo"],
    "Price": [80000,200000,45000],
    "RAM": [8,8,6]
}
df = pd.DataFrame(data,)
df["Storage"] = [128,256,64]
df["Discount"] = df["Price"] * 0.10

new_mobile = pd.DataFrame([{"Brand": "Xiaomi","Price":35000,"RAM":6,"Storage":128}],index=[3])

df = pd.concat([df,new_mobile])
df["Discounted_Price"] = df["Price"] * 0.10

print(df)