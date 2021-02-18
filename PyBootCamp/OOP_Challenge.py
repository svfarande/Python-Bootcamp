class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"{amount} Money deposited. Now balance is : {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"{amount} Money withdraw. Now balance is : {self.balance}")
        else:
            print(f"You don't have enough balance to withdraw {amount} money. Your balance is : {self.balance}")

    def __str__(self):
        return f"Account Owner : {self.owner}\nAccount Balance : {self.balance}"


acct1 = Account("Shubham", 1000)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(500)
acct1.withdraw(750)
acct1.withdraw(5000)
