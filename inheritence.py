
class BankAccount:
    def deposit(self):
        print("Money deposited")

    def check_balance(self):
        print("Checking your balance")


class SavingsAccount(BankAccount):
    def earn_interest(self):
        print("You earn interest")


class CurrentAccount(BankAccount):
    def withdraw(self):
        print("Money withdrawn")


# Create a savings account
s = SavingsAccount()

s.deposit()
s.check_balance()
s.earn_interest()