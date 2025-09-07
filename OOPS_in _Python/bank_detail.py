# Define a class named 'account'
class account:
    # Constructor to initialize balance and account number
    def __init__(self, bal, acc):
        self.bal = bal    # Instance variable for account balance
        self.acc = acc    # Instance variable for account number

    # Method to debit (withdraw) money from the account
    def debit(self, amount):
        self.bal -= amount    # Subtract the amount from balance
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_bal())  # Show updated balance

    # Method to credit (deposit) money into the account
    def creadit(self, amount):   # (typo: should be 'credit')
        self.bal += amount    # Add the amount to balance
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_bal())  # Show updated balance

    # Method to check current balance
    def get_bal(self):
        return self.bal

# Create an account object with balance 10000 and account number 1234
acc1 = account(10000, 1234)

# Debit 1000 from the account
acc1.debit(1000)

# Credit 500 to the account
acc1.creadit(500)