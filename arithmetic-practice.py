monthly_fee = 2500
months = 4
late_fee_percent = 6
scholarship_percent = 15
Total_amount = monthly_fee * months
Scholarship_amount = Total_amount * scholarship_percent / 100
Fee_after_scholarship = Total_amount - Scholarship_amount
late_fee = Fee_after_scholarship * late_fee_percent / 100
Total_fee = Fee_after_scholarship + late_fee
print("The final amount is", Total_fee)
