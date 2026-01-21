Number1 = int(input("Enter a number: "))
Number2 = int(input("Enter a number: "))
Number3 = int(input("Enter a number: "))
if Number1 >= Number2 and Number1 >= Number3:
    print(Number1,"is the greatest")
elif Number2 >= Number1 and Number2 >= Number3:
    print(Number2,"is the greatest")
else:
    print(Number3,"is the greatest")