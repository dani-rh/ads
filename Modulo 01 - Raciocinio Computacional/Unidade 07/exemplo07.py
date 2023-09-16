'''Exemplo de aplicação 7: Salve uma lista de números inteiros em um arquivo chamado “dados.pickle”.'''

import pickle

dados = [1, 2, 3, 4, 5]

with open("dados.pickle", "wb") as arquivo:
    pickle.dump(dados, arquivo)