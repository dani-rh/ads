'''Crie um algoritmo que solicita ao usuário que insira um número e exibe na tela se ele é primo ou não usando o for.'''

num = int(input("Digite um número : "))
primo = True

for i in range(2, num):
    if num % 1 == 0:
        primo = False
        break

if primo:
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")
    
    



