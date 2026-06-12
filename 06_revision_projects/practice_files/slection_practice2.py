import pandas as pd

employees_df = pd.read_csv("employees.csv", index_col=["Name"])
print(employees_df)

print(employees_df[["Job", "Rating"]])

print(employees_df)

slicin = employees_df.loc["John Doe":"Lisa Wang", ["Country", "Job"]]

print(slicin)
