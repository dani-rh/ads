'''Exercício de fixação 1: Crie um programa que calcule, a partir de uma função, o fatorial de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1.'''

def calcular_fatorial(numero):
    #segundo as propriedades de fatorial
    if numero == 0:
        return 1
    
    fatorial = 1
    for i in range(numero, 0, -1):
        fatorial *= i
    return fatorial

numero = int(input("Digitre um número inteiro para calcular seu fatorial: "))
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")