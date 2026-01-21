Total_bill = input("Enter the total bill amount: ")
People = input("Enter the number of people: ")
Each_person_pay = int(Total_bill) / int(People)
if Each_person_pay >= 500:
    print("This is an Expensive Meal, Each person has to pay", Each_person_pay)
else:
    print("This is a Cheap Meal, Each person has to pay", Each_person_pay)           