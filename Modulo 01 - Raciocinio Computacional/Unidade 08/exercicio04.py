'''Crie uma classe Carro com as seguintes funcionalidades:

Um veículo tem certo consumo de combustível (medido em km/l) e certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método abastecer(), que abasteça o carro com o valor passado de litros de combustível.
Forneça um método andar(), que simule o ato de dirigir o veículo por certa distância, reduzindo o nível de combustível no tanque de gasolina.
Forneça um método nivel_combustivel(), que retorne o nível atual de combustível.'''

class Carro:
 
    __combustivel = 0
 
    def __init__(self, autonomia):
        self.__autonomia = autonomia
 
    def abastecer(self, litros):
        if litros >= 0:
            self.__combustivel += litros
 
    def andar(self, distancia):
        litros = distancia / self.__autonomia
        if litros >= self.__combustivel:
            print("O carro parou sem combustível!")
            self.__combustivel = 0
        else:
            self.__combustivel -= litros
 
    def nivel_combustivel(self):
        print(f"O carro ainda tem {self.__combustivel:.2f} litros de combustível!")
 
 
if __name__ == '__main__':
    carro = Carro(12)
    carro.abastecer(100)
    carro.andar(1000)
    carro.nivel_combustivel()
    carro.andar(300)