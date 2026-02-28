def checking(password):
    if password == "mypassword":
        return f"Login successful your password is {password}"
    else:
        return "Wrong password"
user_input =(input("Enter the password " ))
result = checking(user_input)
print(result)