import math

class Circulo:
    def __init__(self, raio_circulo, cor_borda, cor_preenchimento):
        self.raio = raio_circulo
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

    def mudar_cor(self, nova_cor_borda, nova_cor_preenchimento):
        self.cor_borda = nova_cor_borda
        self.cor_preenchimento = nova_cor_preenchimento

    def redimensionar_raio(self, novo_raio):
        self.raio = novo_raio
        
# 3 objetos
circulo1 = Circulo(3, "amarelo", "azul")
circulo2 = Circulo(5, "verde", "verde")
circulo3 = Circulo(2, "azul", "roxo")

print(f'O raio do círculo 3 é {circulo3.raio}')
print(f'A área do círculo 3 é {circulo3.calcular_area()}')

circulo3.redimensionar_raio(4)
print(f'O novo raio do círculo 3 é {circulo3.raio}')
print(f'A nova área do círculo 3 é {circulo3.calcular_area()}')

print(circulo1.cor_borda, circulo1.cor_preenchimento)
print(circulo2.calcular_perimetro())