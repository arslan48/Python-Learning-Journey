guests = ["Ali", "Zain", "Ahmed", "Hamza", "Asad"]
i = 0
while i < len(guests):
    if guests[i][0] == "A":
        print(f"{guests[i]} is invited")
    else:
        print(f"{guests[i]} is not invited")
    i +=1