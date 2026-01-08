is_authorised = False

while not is_authorised:
    pin = input("Enter your pin: ") 
    
    if pin == "0000":
        is_authorised = True
        print("Access Granted!")
    elif len(pin) < 4:
        print("Invalid pin (Too short). Try again.")
    else:
        print("Incorrect pin. Not Authorised.")

print("Your current balance is 5000.")