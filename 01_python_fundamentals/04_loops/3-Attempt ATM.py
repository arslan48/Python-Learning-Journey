pin = "jru9"
attempts = 0
while attempts < 3:
    pinn =(input("Enter the pin: "))
    if pin == pinn:
        print("Acess granted!")
        break
    attempts += 1
    print("Wrong PIN. Try again.")
    continue
else:
    print("card block")