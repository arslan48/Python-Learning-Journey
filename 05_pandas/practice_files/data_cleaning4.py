import pandas as pd 

df = pd.read_csv("dirty_gamers.csv") 

df["PlayerName"] = df["PlayerName"].str.strip() 

df = df.fillna({"Score":"None", "PlayerName":"Unknown"})

df["Score"] = df["Score"].replace({"9999":"N/A",
                                   "99999999":"N/A",
                                    "abc": "N/A" })

df["Hours"] = df["Hours"].replace({"Hours":"67"})

print("\nClean Data\n")
print(df)



