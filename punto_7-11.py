class cuentabancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        self.balance += cantidad


    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad


    def aplicar_cuota_manejo(self):
        self.balance *= 0.98

    def mostrar_detalles(self):

        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)

