cart = {
    "milk": 200,
    "bread": 300
}

 
check = cart.get("eggs", "sorry we don't have eggs")
print(check)

Total_bill = sum(cart.values())
print(f"Total bill is {Total_bill}")

cart2 = {
    "milk": 200,
      "bread": 300,
        "butter": 500
    }


remove = cart2.pop("bread")
print(f"I removed Bread. It cost {remove}, but I don't want it anymore.")
Total_bill2 = sum(cart2.values())
print(f"The total bill of cart2 is{Total_bill2}")

grand_total = Total_bill + Total_bill2
print(f"The grand total is: {grand_total}")