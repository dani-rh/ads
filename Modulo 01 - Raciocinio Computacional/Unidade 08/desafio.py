'''Exercício de fixação 5:

Crie uma classe Bomba que simule uma bomba de combustíveis de um posto. A bomba pode injetar dois tipos de combustível: gasolina ou álcool, podendo definir no construtor da classe a quantidade e o valor do litro de cada um. Deve possuir os seguintes métodos:

abastecer_valor(valor, tipo_combustivel), que mostra quantos litros foram colocados no veículo.
abastecer_litros(litros, tipo_combustivel), que mostra o valor no abastecimento.
fechar(), que mostra ao final do dia quanto foi ganho no valor total da bomba e quanto sobrou de cada tipo de combustível.'''

class Bomba:
 
    __total = 0
 
    def __init__(self, gasolina, valor_gasolina, alcool, valor_alcool):
        self.__gasolina = gasolina
        self.__valor_gasolina = valor_gasolina
        self.__alcool = alcool
        self.__valor_alcool = valor_alcool
 
    def abastecer_valor(self, valor, combustivel):
        if combustivel == "gasolina":
            litros = valor / self.__valor_gasolina
            if litros > self.__gasolina:
                print("Não há gasolina suficiente na bomba!")
            else:
                self.__total += valor
                self.__gasolina -= litros
        elif combustivel == "alcool":
            litros = valor / self.__valor_alcool
            if litros > self.__alcool:
                print("Não há álcool suficiente na bomba!")
            else:
                self.__total += valor
                self.__alcool -= litros
        else:
            print("Tipo de combustível inválido!")
 
    def abastecer_litros(self, litros, combustivel):
        if combustivel == "gasolina":
            valor = litros * self.__valor_gasolina
            if litros > self.__gasolina:
                print("Não há gasolina suficiente na bomba!")
            else:
                self.__total += valor
                self.__gasolina -= litros
        elif combustivel == "alcool":
            valor = litros * self.__valor_alcool
            if litros > self.__alcool:
                print("Não há álcool suficiente na bomba!")
            else:
                self.__total += valor
                self.__alcool -= litros
        else:
            print("Tipo de combustível inválido!")
 
    def fechar(self):
        print(f"Valor do dia: R$ {self.__total:.2f}!")
        print(f"Sobraram {self.__gasolina:.2f} litros de gasolina!")
        print(f"Sobraram {self.__alcool:.2f} litros de álcool!")
 
 
if __name__ == '__main__':
    bomba = Bomba(100, 4.3, 100, 3.1)
    bomba.abastecer_valor(100, "gasolina")
    bomba.abastecer_valor(50, "alcool")
    bomba.abastecer_litros(30, "gasolina")
    bomba.abastecer_litros(70, "alcool")
    bomba.fechar()