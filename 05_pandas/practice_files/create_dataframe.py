import pandas as pd

data = {
    "Name": ["Spongebob","Patric","Puff","Gary"],
    "Marks": [45,67,87,94],
    "Grade": ["D","B","A","A+"]
}

data_frame = pd .DataFrame(data,index=range(1,5))
# print(data_frame)

# print(data_frame["Marks"])

print(data_frame.iloc[0])

