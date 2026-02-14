order_list = []
while True:
    item = input("Enter the item name:")

    if item == "ok":
        break

    if len(item) < 3:
        print("Name must be more then 2 characters:")
        continue

    if item == "pizza":
        print("Sorry we dont have pizza:")
        continue

    order_list.append(item)
    print(f"{item} added to list:")
    
print(order_list)