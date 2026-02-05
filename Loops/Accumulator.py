total = 0

num = int(input("Enter a number (0 to stop): "))


while num != 0:
    total += num  
    num = int(input("Enter another number (0 to stop): "))

print(f"Your final total is: {total}")