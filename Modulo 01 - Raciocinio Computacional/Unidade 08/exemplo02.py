'''Exemplo de aplicação 2: Elabore uma classe que simule um dado de jogo. No construtor, deve-se informar quantas faces possui o dado. Caso o valor informado seja inválido, o dado será padrão, de seis faces. Deve ter um método privado de calcular a jogada e um método público de retorno do valor do dado para o usuário. Ao final, deve testar a classe e todos os seus métodos.'''

import random
 
class Dado:
    def __init__(self, faces=6):
        self.__faces = faces if faces > 2 else 6
    def valor_jogada(self):
        return self.__calcular_jogada()
    def __calcular_jogada(self):
        return random.randint(1, self.__faces)
 
if __name__ == '__main__':
    dado4 = Dado(4)
    print(dado4.valor_jogada())
    dado = Dado(1)
    print(dado.valor_jogada())