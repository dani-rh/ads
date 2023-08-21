'''Adapte o código para que tenha uma função chamada verificar_palindromo em que recebe um parâmetro de entrada chamado palavra e retorna True se ele for palíndromo e False se não for palíndromo.'''

def verificar_palindromo(palavra):
    i = 0
    j = len(palavra) - 1
    palindromo = True

    while i < j:
        if palavra[i] != palavra[j]:
            palindromo = False
            break
        i += 1
        j -= 1
        
    return palindromo

palavra_teste = input("Digite uma palavra: ")
eh_palindromo = verificar_palindromo(palavra_teste)

if eh_palindromo:
    print(palavra_teste, "é um palíndromo")
else:
    print(palavra_teste, "não é um palíndromo")