'''Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.'''

contPar = 0
contImpar = 0
for i in range (10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        contPar += 1
    else:
        contImpar += 1
print("Dos 10 números", contPar, "são pares e", contImpar, "são ímpares.")