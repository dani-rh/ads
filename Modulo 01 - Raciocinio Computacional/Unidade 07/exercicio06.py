'''Exercício de fixação 6: Crie um programa que lê o conteúdo do arquivo “exemplo.json” do exercício anterior. Salve o conteúdo em um dicionário. Mostre o conteúdo do dicionário na tela.'''

import json

with open("exemplo.json", "r", encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)
    
print(conteudo)