import pandas as pd

data = {
    "Name": ["Ali","Sara","Usman","Ayesha","Bilal"],
    "Marks": [78,92,55,88,63],
    "Attendance" : [90,95,60,85,70]
}

df = pd.DataFrame(data)
df["Grade"] = ["A+","A","B","C","D"]

top_students = df[df["Marks"] > 80]
print(top_students)

high_marks= df["Marks"].max()
print(df[df["Marks"]== high_marks])

new_student = pd.DataFrame([{"Name": "Ahmed","Marks": 89,"Attendance": 80,"Grade":"A"},
                            {"Name": "Kashif","Marks": 76,"Attendance": 90,"Grade":"B"}],index=[5,6])
df = pd.concat([df,new_student])

print(df)