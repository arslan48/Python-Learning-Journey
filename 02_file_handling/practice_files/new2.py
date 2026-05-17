a = "file2.txt"
with open(a,"w") as file:
    file.write("hi how are you\n")
    file.write("What are you doing.")
with open(a,"a") as changes:
    changes.write("\nNicee")
    changes.write("\namazing")
    changes.write("\nwow")

with open(a) as f:
    content = f.read()
    print(content)