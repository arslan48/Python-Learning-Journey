import pandas as pd
data = {
    "Math": 86,
    "Physics": 92,
    "English": 78,
    "Chemistory": 98,
    "Computer": 79
}

s = pd.Series(data)
s.iloc[4] -= 23

good_marks= s[s> 90]
print(f"You got good marks in these subjects\n {good_marks}")