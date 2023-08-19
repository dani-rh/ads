''' Adapte o código que você fez no exercício 4 para que a função seja chamada dentro de um for. O for deve repetir cinco vezes. A cada iteração você deve pedir para que o usuário digite uma palavra. Com isso, testaremos se cinco palavras diferentes são ou não palíndromos.'''

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

for i in range(5):
    palavra_teste = input("Digite uma palavra: ")
    eh_palindromo = verificar_palindromo(palavra_teste)

    if eh_palindromo:
        print(palavra_teste, "é um palíndromo")
    else:
        print(palavra_teste, "não é um palíndromo")