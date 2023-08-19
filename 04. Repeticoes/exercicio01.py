'''Crie um algoritmo que pede ao usuário para que digite um número inicial e um número final. Em seguida, ele mostrará todos os números pares neste intervalo usando for.'''

inicial = int(input("Digite um número inicial: "))
final = int(input("Digite um número final: "))

for num in range(inicial, final+1):
    if num % 2 == 0:
        print(num, "é um número par")

