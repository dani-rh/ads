'''Exemplo de aplicação 8: Leia o conteúdo do arquivo “dados.pickle” e armazene-o em uma variável chamada “variavel_lida”.'''

import pickle

with open("dados.pickle", "rb") as arquivo:
    variavel_lida = pickle.load(arquivo)
    
print(variavel_lida)