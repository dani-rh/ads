def maior_menor(*numeros):
    maior = -1000000
    menor = 100000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor

resultado = maior_menor(7, 15, 3, 22, 1, 8)
print(f"O maior número é {resultado[0]} e o menor número é {resultado[1]}")

