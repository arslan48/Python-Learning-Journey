import pandas as pd

df = pd.read_csv("employees.csv",index_col=["Name"])
# print(df)
print("\nLast Five Rows Data\n")
print(df.iloc[-5:])

print("\nMike Davis info\n")
print(df.loc["Mike Davis"])

print(df.iloc[10:16])

print("\nSphie Martin Rating\n")
print(df.loc["Sophie Martin", "Rating"])

print(df[["Job","Salary"]])

