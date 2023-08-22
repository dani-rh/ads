#input e print

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# soma = num1 + num2
# print(soma)

#formatando strings
# 1 - concatenando
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma dos números " + str(num1) + " e " + str(num2) + " é: "+ str(soma))

# 2 - usando f-strings
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print(f"A soma dos números {num1} e {num2} é: {soma}")

# 3 - usando placeholders
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma dos números {} e {} é: {}".format(num1, num2, soma))

# 4 - usando format()
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
print("A soma dos números {1} e {2} é: {0}".format(soma, num1, num2))