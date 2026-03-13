import os  

filename = "expenses.txt"


if os.path.exists(filename):
    os.remove(filename)  
    print(f"Bhai, {filename} file deleted!")
else:
    print("File not exit?")