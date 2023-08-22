soma = 0
num = -1
while num != 0:
    num = int(input("Digite um número para somar (0 finaliza): "))
    soma += num
print("A soma dos números é ",soma)

soma = 0
num = -1
while True:
    num = int(input("Digite um número para somar (0 finaliza): "))
    if num == 0:
        break
    soma += num
print("A soma dos números é ", soma)