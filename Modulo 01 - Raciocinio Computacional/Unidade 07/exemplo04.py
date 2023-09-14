'''Exemplo de aplicação 4: Leia novamente o conteúdo do arquivo “nome.txt”. Agora, leia uma linha de cada vez, e mostre o conteúdo de cada linha na tela.'''

with open("nome.txt", "r") as f:
    for linha in f.readlines():
        print(linha)