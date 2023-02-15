class rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2

    def calcular_perimetro(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return 2 * (base + altura)

    def calcular_area(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base * altura

    def es_cuadrado(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base == altura
