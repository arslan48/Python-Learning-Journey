import pandas as pd

df = pd.read_json("students_150.csv")
print(df.to_string())