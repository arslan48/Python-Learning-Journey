# 1. Get user inputs
# We use 'snake_case' for variable names which is standard in Python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
money = int(input("How much money do you have? "))

# 2. Define VIP list and ticket price
vip_list = ["John", "Doe", "Jane"]
ticket_price = 20

# 3. Check access logic
if name in vip_list:
    # VIPs enter for free
    print("Welcome back! Your ticket is free.")

elif 18 <= age < 60:
    # If not VIP, check if age is allowed (18 to 59)
    if money >= ticket_price:
        # Check if they have enough money
        balance = money - ticket_price
        print("Welcome to the party! Your remaining balance is", balance)
    else:
        print("Sorry, you don't have enough money.")

else:
    # If age is too young or too old
    print("Sorry, you are not allowed to enter.")
