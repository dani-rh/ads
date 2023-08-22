'''Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela se ele é positivo, negativo ou zero.'''

num = float(input("Insira um número: "))

if num > 0:
    print("Positivo!")
elif num == 0:
    print("Zero!")
else:
    print("Negativo!")