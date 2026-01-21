units = int(input("Enter the units consumed: "))
cost_per_unit = 35
service_tax = 150

# Calculate total amount
total_amount = (units * cost_per_unit) + service_tax

if total_amount >= 2000:
    print("Safe Electricity usage. The total amount is", total_amount)
elif total_amount >= 1000:
    print("Good Electricity usage. The total amount is", total_amount)
else:
    print("Excellent! The total amount is", total_amount)