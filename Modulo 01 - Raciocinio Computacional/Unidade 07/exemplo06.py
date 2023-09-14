'''Exemplo de aplicação 6: Leia o conteúdo do arquivo “pessoa.json” e armazene-o em uma variável chamada dados_lidos.'''

import json

with open("pessoa.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)
    
print(dados_lidos)