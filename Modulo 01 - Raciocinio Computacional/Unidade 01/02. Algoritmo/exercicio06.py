'''Crie um algoritmo que solicita ao usuário que insira a sua altura em metros e o seu peso em quilogramas e exibe na tela o seu índice de massa corporal (IMC).'''

# Solicita altura e peso
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilogramas: "))

# Calcula o IMC
imc = peso/altura ** 2 #altura**2 é igual a altura elevado a 2

print("Seu IMC é: ",imc)

