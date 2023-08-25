'''Exercício de fixação 1: Crie um programa que solicite ao usuário seis números, calculando a média, e mostre uma lista com os números iguais ou acima da média e uma lista com os números abaixo da média.'''

numeros = []
maiores = []
menores = []
soma = 0
for _ in range (6):
    num = float(input("Digite o número: "))
    numeros.append(num)
    soma += num
media = soma / 6
for num in numeros:
    if num >= media:
        maiores.append(num)
    else:
        menores.append(num)
print("A média dos 6 números é", media)
print("Os números iguais ou maiores que a média são", maiores)
print("Os números menores que a média são", menores)
