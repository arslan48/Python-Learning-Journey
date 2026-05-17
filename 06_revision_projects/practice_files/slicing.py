menu = {"Pizza": 1200, "Burger": 500, "Coke": 150, "Fries": 200}

my_order = ["Pizza", "Fries", "Coke"]

total_bill = 0

for item in my_order:
    if item in menu:
        price = menu[item]
        total_bill += price

print(f" Total bill {total_bill} ")
