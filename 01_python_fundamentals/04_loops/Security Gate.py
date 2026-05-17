code = "fjru2"
acess_granted = False
while acess_granted == False:
    passcode = input("Enter the code: ")
    age = int(input("Enter the age: "))
    if (passcode == code and age >= 18):
        print("acess granted")
        break
    else:
        print("not granted")