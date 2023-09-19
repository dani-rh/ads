'''Exercício de fixação 2: Crie uma classe de cartas de baralho com o nome de Carta. Ao imprimir a carta, deve ser mostrada uma carta de 1 a 10 ou figuras (dama, valete ou rei) e um naipe (ouros, espadas, copas ou paus).'''

import random
 
 
class Carta:
    __valor = 0
    __valores = ["1", "2", "3", "4", "5", "6", "7", "7", "9", "10", "dama", "valete", "rei"]
    __naipe = 0
    __naipes = ["ouros", "espadas", "copas", "paus"]
 
    def __init__(self):
        self.__sortear()
 
    def imprimir(self):
        print(self.__valores[self.__valor], "de", self.__naipes[self.__naipe])
        self.__sortear()
 
    def __sortear(self):
        self.__valor = random.randint(0, len(self.__valores) - 1)
        self.__naipe = random.randint(0, len(self.__naipes) - 1)
 
 
if __name__ == '__main__':
    carta = Carta()
    for i in range(5):
        carta.imprimir()
