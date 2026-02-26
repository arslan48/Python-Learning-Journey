emails = [" ali@gmail.com", "zain@yahoo.com", "  sara@gmail.com ", "hamza@outlook.com", "dua@gmail.com"]
for i in range(len(emails)):
    emails[i] = emails[i].strip()
    if emails[i].endswith("@gmail.com"):
     print(emails[i])