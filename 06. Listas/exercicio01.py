'''Crie uma lista com números de 1 a 10 e, em seguida, imprima apenas os números pares.'''

numeros = list(range(1,11))

for num in numeros:
    if num % 2 == 0:
        print(num)