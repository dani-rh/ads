fatorial = 1
expressao = "Expressão: "
num =  int(input("Digite um número para o cálculo do fatorial: "))
for i in range (num, 0, -1):
    fatorial *= i
    expressao += str(i)
    if i > 1:
        expressao += " * "
print("O valor do fatorial de", num, "é", fatorial,expressao)