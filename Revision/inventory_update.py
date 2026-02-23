stock = {"Apples": 50, "Bananas": 10, "Oranges": 0, "Grapes": 5}
for fruit, quantity in stock.items():
    if quantity == 0:
        print(f"{fruit} is out of stock ! ")
    elif quantity < 10:
        print(f"{fruit} is low! Only {quantity} left.")
    else:
        print(f"{fruit} is available ({quantity} units).")