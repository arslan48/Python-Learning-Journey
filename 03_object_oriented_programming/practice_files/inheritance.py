class Account():
    def __init__(self,balance):
        self.balance = balance
    def check_balance(self):
        print(f"Your balance is: {self.balance}")

class Saving_Account(Account):
    def add_interest(self):
        self.balance = self.balance + 500
        print("Interest added successfully!")

my_acc = Saving_Account(5000)
my_acc.check_balance()
my_acc.add_interest()
my_acc.check_balance()
