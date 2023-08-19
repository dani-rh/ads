'''Escreva uma função que recebe como parâmetro uma temperatura em graus Celsius. Ela deve retornar a temperatura convertida para graus Fahrenheit.'''

def converter_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

temperatura = 0
print("A temperatura em Fahrenheit é:",converter_fahrenheit(temperatura))