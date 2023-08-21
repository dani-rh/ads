'''Crie um dicionário com o nome e a idade de três pessoas e exiba a idade de cada uma delas na tela.'''

pessoas = {'João':25, 'Maria': 30, 'José': 40}

for nome, idade in pessoas.items():
    print(f'{nome} tem {idade} anos.')
           