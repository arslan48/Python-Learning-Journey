cart2 = {
    "milk": 200,
      "bread": 300,
        "butter": 500
    }


remove = cart2.pop("bread")
print(f"I actually dont want: {remove}")
Total_bill2 = sum(cart2.values())