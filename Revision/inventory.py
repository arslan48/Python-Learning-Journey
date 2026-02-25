inventory = {"apples": 10, "bananas": 5, "oranges": 0}

# Check stock
for item in inventory:
    if inventory[item] == 0:
        print(item, "Out of stock!")
    elif 1 <= inventory[item] <= 5:
        print(item, "Low stock")

# Sell a fruit
fruit = input("Enter a fruit to buy: ")
if fruit in inventory and inventory[fruit] > 0:
    inventory[fruit] -= 1
    print("One", fruit, "sold. Remaining:", inventory[fruit])
else:
    print(fruit, "is not available")