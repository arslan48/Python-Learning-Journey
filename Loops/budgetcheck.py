budget = 1000
expense_list = []
while budget > 0:
    item = input("What do you want: ")
    price = int(input("How much did it cost: "))
    if price > budget:
        print("you have not enough money to buy this item ")
        continue

    budget -= price
    expense_list.append(item)
    print(f"Remaining money: {budget}")
    if budget == 0:
        print("You have reached your budget limit")
        break
        
print(f"Your budget limit has been reached. You bought these items:\n {expense_list}")
