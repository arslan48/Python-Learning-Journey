def login_system():
    for i in range(3):
        username = input("Enter name: ")
        password = input("Enter the password:")
        if  username == "Ahmed" and password == "ffhr12":
            return "Login sucessfull"
        else:
            print(f"please try again {2 -i} attempts are left ")
    return "Account blocked"
print(login_system())