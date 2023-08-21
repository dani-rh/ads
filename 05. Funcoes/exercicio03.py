'''Adapte o código abaixo para que tenha uma função chamada verificar_primo em que recebe um parâmetro de entrada chamado numero e retorna True se ele for primo e False se não for primo.'''
def verificar_primo(numero):
    primo = True
    
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
    return primo

num = int(input("Digite um número: "))
if verificar_primo(num):
    print(num, "é um número primo")
else:
    print(num, "não é um número primo")