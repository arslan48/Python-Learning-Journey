import pandas as pd 

df = pd.read_csv("dirty_heroes.csv")

# print(df)

df =df.fillna({"Name":"Superman"})

print("\nFix missing name\n")
print(df)

df = df.drop_duplicates()
print("\nRemove duplicates\n")
print(df)

df["Name"] = df["Name"].replace({" Iron Man ":"IronMan"})
print("\nFix spaces\n")
print(df)

df["Strength"] = df["Strength"].replace({"99999":"87",
                                        "abc":"Not found"})
print("\nfix strength\n")
print(df)

df = df.fillna({"Universe": "Marvel"})
print("\nAdd universe\n")
print(df)
