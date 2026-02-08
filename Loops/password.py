secret_passcode = "43rf32"


user_input = input("Enter the passcode: ") 

while user_input != secret_passcode:

    print(f"Passcode {user_input} is incorrect!")
    
    user_input = input("Please try again: ")


print(f"Passcode is correct: {user_input}")
