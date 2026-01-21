Item_Name = input("Enter the item name: ")
Target_Price = float(input("How much the item costs: "))
Saving = float(input("How much you saved: "))
remaining_amount = Target_Price - Saving
if Saving >= Target_Price:
    print("Congrulation you can buy the item", Item_Name)
elif Saving > (Target_Price / 2):
    print(f"You are more than halfway there! You only need {remaining_amount} more.")
else:
    print("You need to save more")
    