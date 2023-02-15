class cuentabancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f'Se han depositado {monto} en la cuenta. Nuevo balance: {self.balance}')

    def retirar(self, monto):
        if self.balance < monto:
            print('Fondos insuficientes')
        else:
            self.balance -= monto
            print(f'Se han retirado {monto} de la cuenta. Nuevo balance: {self.balance}')
