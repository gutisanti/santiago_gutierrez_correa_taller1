class cuentabancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= monto

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
