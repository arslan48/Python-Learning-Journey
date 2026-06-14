import pandas as pd
movies_df = pd.read_csv("movies_data.csv")
# print(movies_df)

cleaned_df =(
	movies_df
	.dropna(subset=["Title","BoxOffice"])
	.drop_duplicates()
	.copy()
)
cleaned_df["Title"] = cleaned_df["Title"].str.strip()
cleaned_df["Rating"] = cleaned_df["Rating"].replace({"abc":"-"}).fillna("-")

print(cleaned_df)
