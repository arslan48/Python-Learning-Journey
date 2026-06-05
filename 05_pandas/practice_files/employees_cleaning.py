import pandas as pd 

df= pd.read_csv("employees.csv")
print(df)
e = df[df["Country"]=="Pakistan"]
print(e)

s = df[(df["Salary"] > 100000) & (df["Country"] == "Pakistan")]
print("\nPakistan employees salary is more then 100000\n")
print(s)

d = df[(df["Job"]== "Developer") & (df["Rating"]> 8.5)]
print("\nDeveloper  with rating  8.5\n")
print(d)
