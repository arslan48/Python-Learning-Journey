is_Unlock = False
while not is_Unlock:
    pin = input("Enter your pin: ")
    if pin == "0000":
        is_Unlock = True
        print("Phone unlocked")
    else:
        print("Incorrect pin")
        
