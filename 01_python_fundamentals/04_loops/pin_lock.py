passcode = 4351

inpu = int(input("Enter the passcode"))
while inpu!= passcode:
    
    print(f"incorrect passcode: {inpu}")
    inpu = int(input("Try again: ")) 
print("Acess Granted")