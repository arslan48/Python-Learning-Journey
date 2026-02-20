balance = 10000
while balance > 500:
    withdraw = int(input("How much money do you want to withdraw: "))
    if withdraw <= balance:
        balance -=withdraw
        print(f"Remaing balance {balance}")
    else:
        print("In-sufficient funds!")
print("Account Locked: Minimum balance reached")