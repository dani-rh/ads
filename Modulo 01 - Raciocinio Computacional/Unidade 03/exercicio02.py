'''Crie um programa que peça ao usuário cinco números e informe qual é o menor e qual é o maior deles.'''
menor = 1000000
maior = -1000000

for i in range(5):
    num = int(input("Digite um número: "))
    if num < menor:
        menor = num
    if num > maior:
        maior = num
print("O menor número é",menor, "e o maior número é",maior)
    
