import math

class Forma:
    def calcular_area(self):
        return "Ainda não tenho uma lógica implementada para calcular esta área."
    
    def calcular_perimetro(self):
        return "Ainda não tenho uma lógica implementada para calcular este perímetro."

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
    def redimensionar_raio(self, novo_raio):
        self.raio = novo_raio

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def redimensionar_base(self, nova_base):
        self.base = nova_base
        
    def redimensionar_altura(self, nova_altura):
        self.altura = nova_altura
        
circulo1 = Circulo(3)
retangulo1 = Retangulo(10, 2)

print(circulo1.calcular_area())
print(circulo1.calcular_perimetro())

print(retangulo1.calcular_area())
print(retangulo1.calcular_perimetro())