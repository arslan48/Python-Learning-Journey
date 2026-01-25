customer_data = {"name": "zain khan", "item": "gaming mouse"}
price = 1500
quantity = 3
discount_percent = 10


print(f"Customer: {customer_data['name'].title()}\nItem: {customer_data['item'].upper()}\nTotal: {price*quantity}\nFinal: {(price*quantity)*0.9}")