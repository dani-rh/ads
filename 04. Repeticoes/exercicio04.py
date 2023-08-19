'''Crie um algoritmo para calcular o fatorial de um número usando o for.'''

num = int(input("Digite um número: "))

fatorial = 1
for i in range (1, num+1):
    fatorial *= i

print("O fatorial de", num, "é", fatorial)