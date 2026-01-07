acess_granted = False

while not acess_granted:
    password = int(input("Enter your password: "))
    
    if password == 123456:
        acess_granted = True
        print("Access granted")
    else:
        print("Access denied. Try again.")