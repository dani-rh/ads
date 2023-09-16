'''Exemplo de aplicação 9: Adicione um tratamento de exceções para um algoritmo que pede ao usuário para que ele(a) digite um número e, em seguida, dividisse aquele número por zero.'''

numero = int(input("Digite um número: "))

try:
    print(numero/0.0)
except:
    print("Não foi possível dividir o número por zero.")