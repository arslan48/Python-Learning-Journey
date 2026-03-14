import os 
file = "nn.txt"
input = input("Friends, what should be done? (d for delete, r for rename:")

if input == "d":
    if os.path.exists(file):
        print("file sucessfully deleted:")
    else:
        print("file not found, cannot delete")
elif input == "r":
    if os.path.exists(file):
        os.rename(file,"my_notes.txt")
        print(f"file name changed to my_notes.txt")
    else:
        print("file not found, cannot rename")
else:
    print("invalid input please enter d or r")