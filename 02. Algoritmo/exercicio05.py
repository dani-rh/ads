'''Crie um algoritmo que solicita ao usuário que insira a temperatura em graus Celsius e exibe na tela a temperatura em Fahrenheit.'''

#Solicita a temperatura
temp_celsius = float(input("Insira a temperaruta em graus Celsius: "))
#Converte para Fahrenheit
temp_faren = (temp_celsius * 9/5) + 32
#Exibe a temperatura em Fahrenheit
print("A temperatura em graus Fahrenheit é: ",temp_faren)