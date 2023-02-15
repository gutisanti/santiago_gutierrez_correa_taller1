class BankAccount:
    def __init__(self, account_number, owners, balance):
        self.account_number = account_number
        self.owners = owners
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
