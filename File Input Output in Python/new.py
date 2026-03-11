file_path = "daily_log.txt"

with open(file_path, "w") as file:
    file.write("hi\n")
    file.write("hellow\n")
    file.write("Today I learned file handling in Python.")




with open(file_path, "a") as a:
    a.write("\nThis is the new line I am appending.")
    a.write("\n Nice")
    a.write("\nwonderfull")


with open(file_path, "r") as f:
    updated_content = f.read()
    print(updated_content)