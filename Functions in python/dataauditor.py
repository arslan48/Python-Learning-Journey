def atm():
    correct_pin = "1234"
    
    for i in range(3):
        pin_input = input(f"Attempt {i+1}: Enter the pin: ")
        
        if pin_input == correct_pin:
            amount = input("Enter the amount to withdraw: ")
            return f"Login successful! Amount {amount} withdrawn."
        
        else:
            print(f"Wrong PIN. You have {2-i} attempts left.")
            
    return "Card blocked! Please contact your bank." 
# Function Call
print(atm())


