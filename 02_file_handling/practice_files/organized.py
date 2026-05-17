import os

folder_name = "MyData"


if not os.path.exists(folder_name):
    os.mkdir(folder_name)


file_path = "MyData/test.txt" 

with open(file_path, "w") as f:
    f.write("this file is in folder!")

print("Done!")