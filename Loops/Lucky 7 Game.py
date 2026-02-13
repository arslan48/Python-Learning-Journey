lucky_number = 7
while True:
    number = int(input("Enter the number: "))
    if number < 0:
        print("Negative numbers are not allowed ❌")
        continue
    if number == lucky_number:
        print("you won the prize 🎉 ")
        break
    else:
        print("please try again ❌")