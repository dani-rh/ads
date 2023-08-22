'''Crie um programa que gere a série de Fibonacci enquanto o valor for menor que um valor informado pelo usuário. Observação: série de Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55, ... é formada por 0, 1 e, partir deste ponto, sempre será a soma dos dois valores anteriores.'''

valor = 0
max = int(input("Informe o valor-limite: "))
num1 = 0
num2 = 1
serie = "0, 1"
while valor < max:
    valor = num1 + num2
    if valor < max:
        num1 = num2
        num2 = valor
        serie += ", " + str(valor)
print("Fibonacci:", serie)