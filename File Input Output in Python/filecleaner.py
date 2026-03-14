import os
file = "tempdata.txt"
task = input("delete file? ")
if task == "y":
    if os.path.exists(file):
        os.remove(file)
        print(f"File {file} sucessfully deleted.")
    else:
        print("file don't exit")
else:
    print("file saved")