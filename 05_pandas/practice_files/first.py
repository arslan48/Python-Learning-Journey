import pandas as pd 
data = [78,500,34,]
s = pd.Series(data,index=["a","b","c"])
s.loc["c"] = 48
print(s.loc["c"])

# Student Marks

subjects = ["Math", "English","Physics","Chemistry", "Computer"]
marks = [85,90,78,92,88]

mark = pd.Series(marks,index=subjects)
print(f"Physics marks: {mark.loc['Physics']}")
print(f"Maths marks: {mark.iloc[0]}")
print(f"{subjects[-1]} marks: {mark.iloc[-1]}")

# Filter student marks 

print("\nFiltered marks (>= 90):")
print(mark[mark >= 90])
print("\nFiltered marks (< 80):")
print(mark[mark < 80])