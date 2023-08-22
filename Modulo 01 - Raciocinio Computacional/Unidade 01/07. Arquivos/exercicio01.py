'''Crie um dicionário com o nome e a profissão de duas pessoas e adicione uma terceira pessoa com nome e profissão. Salve o resultado em um arquivo JSON.'''

import json

pessoas = {}

#adiciona as duas primeiras pessoas
for i in range (2):
    nome = input("Digite o nome da pessoa: ")
    profissao = input("Digite a profissão da pessoa:")
    pessoas[nome] = profissao
    
#adiciona a terceira pessoa
nome = input("Digite o nome da pessoa: ")
profissao = input("Digite a profissão da pessoa:")
pessoas[nome] = profissao

#salva o resultado em um arquivo JSON
with open("pessoas.json","w") as arquivo:
    json.dump(pessoas,arquivo)