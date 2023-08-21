import math

class Circulo:
    def __init__(self, raio_circulo, cor_borda, cor_preenchimento):
        self.__raio = raio_circulo
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def calcular_area(self):
        return math.pi * self.__raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.__raio

    def mudar_cor(self, nova_cor_borda, nova_cor_preenchimento):
        self.cor_borda = nova_cor_borda
        self.cor_preenchimento = nova_cor_preenchimento

    def redimensionar_raio(self, novo_raio):
        self.__raio = novo_raio

    def __metodo_privado(self):
        print("Este é um método privado.")