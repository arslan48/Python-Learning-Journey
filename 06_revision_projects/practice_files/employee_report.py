import pandas as pd

# Load employee data and use the Name column as the row index
employees_df = pd.read_csv("employees.csv", index_col="Name")

# Show the full employee table
print(employees_df)

# Show only the Salary column for all employees
print(employees_df["Salary"])

# Show the first five rows of the table
print(employees_df.iloc[0:5])

# Show all data for the employee named Ahmed Siddiqui
print(employees_df.loc["Ahmed Siddiqui"])

# Show rows 4 through 8 (0-based index)
print(employees_df.iloc[3:8])

# Show the Salary value for the employee named Zara Khan
print(employees_df.loc["Zara Khan", "Salary"])

