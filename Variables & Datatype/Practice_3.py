Age = int(input("Enter your age: "))
Account_Status = input("Enter your account status(active/inactive): "). lower()
Phone_Verification = input("Enter your phone verification status(yes/no): "). lower()
if Age >= 18 and Account_Status == "active" and Phone_Verification == "yes":
    print("You have full access to use this app")
elif Age >= 18 and (Account_Status == "active" or Phone_Verification == "yes"):
    print("You have limited access to use this app")
else:
  print("You have no access to use this app")