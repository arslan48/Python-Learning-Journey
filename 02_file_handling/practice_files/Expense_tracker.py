while True:
    item = input("item name:")
    if item == "stop":
        break
    price = int(input("price:"))
    with open("expenses.txt","a") as f:
        f.write(f"Item: {[item]} - Price: {[price]}\n ")
print("visit a file ")
