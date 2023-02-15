class BankAccount:
    def __init__(self, account_number, owners, balance):
        self.account_number = account_number
        self.owners = owners
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def aplicar_cuota_manejo(self):
        self.balance *= 0.98
