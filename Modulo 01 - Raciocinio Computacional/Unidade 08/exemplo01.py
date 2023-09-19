'''Exemplo de aplicação 1: Elabore uma classe Quadrado, que receba em seu construtor o lado e tenha como função para seus métodos calcular perímetro, área e diagonal, bem como um método de impressão informando: “Quadrado de lado {lado}”. Ao final, deve testar a classe e todos os seus métodos.'''

import math
 
 
class Quadrado:
 
    def __init__(self, lado):
        self.__lado = lado if lado >= 0 else 0
 
    def calc_perimetro(self):
        return self.__lado * 4
 
    def calc_area(self):
        return self.__lado ** 2
 
    def calc_diagonal(self):
        return self.__lado * math.sqrt(2)  # math.sqrt calcula raiz quadrada
 
    def imprimir(self):
        print("Quadrado de lado", self.__lado)
 
 
if __name__ == '__main__':
    quadrado = Quadrado(5)
    quadrado.imprimir()
    print("Perímetro:", quadrado.calc_perimetro())
    print("Área:", quadrado.calc_area())
    print(f"Diagonal: {quadrado.calc_diagonal():.2f}")