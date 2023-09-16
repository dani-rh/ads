'''Exercício de fixação 5: Crie um programa que salva uma lista de dicionários em um arquivo chamado “exemplo.json” usando como base a lista abaixo:'''
import json

dados = [
    {"nome": "João", "idade": 25, "cidade": "Curitiba"},
    {"nome": "Maria", "idade": 30, "cidade": "São Paulo"},
    {"nome": "Carlos", "idade": 28, "cidade": "Rio de Janeiro"}
]

with open("exemplo.json", "w", encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)
    

