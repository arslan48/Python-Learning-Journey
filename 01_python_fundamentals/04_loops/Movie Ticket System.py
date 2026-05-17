ticeket_issued = False
while ticeket_issued == False:
    age = int(input("Enter the age: "))
    Money = int(input("How much money do you have: "))
    Id_card = input("Do you have an id card (yes/no): ")
    Parental_Permission = input("Do you have parental premission (yes/no): ")
    if Money >= 500 and (age >= 18 and Id_card == "yes" or Parental_Permission == "yes"):
        print("ticket issued")
        break
    else:
        print("Sorry you dont fullfil the criteria: ")