import math

class Circulo():
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        area = math.pi*self.raio **2
        return area
    def calcular_circunferencia(self):
        circunferencia = 2*math.pi*self.raio
        return circunferencia

class Cilindro(Circulo):
    def __init__(self, raio, altura):
        super().__init__(raio)
        self.altura = altura

    def calcular_volume(self):
        volume = self.calcular_area()*self.altura
        return volume


cilindro1 = Cilindro(10, 10)
print(f"Volume do cilindro é: {cilindro1.calcular_volume()}")



