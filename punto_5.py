import math

class circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        distancia = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia <= self.radio
