while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if not username or not password:
        print("Username or password cannot be empty.")
    elif len(password) < 8:
        print("Password must be at least 8 characters long.")
    else:
        print("Login successful.")
        break
