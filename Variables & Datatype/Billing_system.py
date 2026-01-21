price_per_item = 120
quantity = 7
discount_percent = 10
tax_percent = 5
Total_amount = price_per_item * quantity
Discount_amount = Total_amount * discount_percent / 100
Tax_amount = Total_amount * tax_percent / 100
Final_amount = Total_amount - Discount_amount + Tax_amount
print("The total amount is", Final_amount)