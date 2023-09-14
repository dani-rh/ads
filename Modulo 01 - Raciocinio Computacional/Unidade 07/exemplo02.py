'''Exemplo de aplicação 2: Usando o exemplo de aplicação 1, leia o nome salvo no arquivo “nome.txt”, mostrando cada caractere em uma linha separada.'''

with open("nome.txt", "r") as f:
    conteudo = f.read()

    for letra in conteudo:
        print(letra)