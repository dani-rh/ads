'''Crie um algoritmo que peça ao usuário três números e informe qual deles é o maior.'''

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

if num1 >= num2 and num1 >= num3:
    print("O número 1 é o maior.")
elif num2 >= num1 and num2 >= num3:
    print("O número 2 é maior.")
else:
    print("O terceiro número é maior.")
