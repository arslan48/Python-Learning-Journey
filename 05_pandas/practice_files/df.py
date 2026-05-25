import pandas as pd

data = {
    "Name": ["Alice","Bob","Carlo","Max"],
    "Age": [43,34,54,65],
    "Country": ["Japan","England","China","Iran"]
}

df = pd.DataFrame(data,index=range(1,5))
# print(df)

print(df.iloc[0])

print(df["Country"])