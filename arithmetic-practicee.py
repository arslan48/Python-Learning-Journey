monthly_fee = int(input("Enter the monthly fee: "))
months = int(input("Enter the number of months: "))

print("Admin decided to add late fee percentage according to how many days late it is")
late_fee_percent = int(input("Enter the late fee percentage: "))

print("Admin decided to give scholarship percentage according to how many marks the student got")
scholarship_percent = int(input("Enter the scholarship percentage: "))

total_amount = monthly_fee * months
scholarship_amount = total_amount * scholarship_percent / 100
fee_after_scholarship = total_amount - scholarship_amount

late_fee = fee_after_scholarship * late_fee_percent / 100
total_fee = fee_after_scholarship + late_fee

print("The final amount is", total_fee)
