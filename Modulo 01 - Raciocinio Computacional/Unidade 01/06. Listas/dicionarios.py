# pessoa = {
#     "nome": "João",
#     "idade": 30,
#     "cidade": "São Paulo"
# }
# print(pessoa)

# # Percorrendo um dicionário
# # criação de um dicionário com algumas informações
# pessoa = {
#     "nome": "João",
#     "idade": 30,
#     "cidade": "São Paulo"
# }

# # percorrendo as chaves do dicionário
# for chave in pessoa:
#     print(chave)
    
# for chave in pessoa.keys():
#     print(chave)
    
# # percorrendo os valores do dicionário
# for valor in pessoa.values():
#     print(valor)
    
# # percorrendo as chaves e valores do dicionário ao mesmo tempo
# for chave, valor in pessoa.items():
#     print(chave, valor)
    
# # criação de um dicionário com algumas informações
# estoque = {
#     'banana': 10,
#     'maçã': 5,
#     'laranja': 8
# }

# # percorrendo as chaves e valores do dicionário e exibindo informações sobre o estoque
# for chave, valor in estoque.items():
#     print(f"Temos {valor} unidades de {chave} em estoque.")
    
# # Adicionando elementos
# pessoa = {
#     "nome": "João",
#     "idade": 30,
#     "cidade": "São Paulo"
# }

# pessoa["profissao"] = "engenheiro"
# print(pessoa)

# # Removendo elementos
# meu_dicionario = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# del meu_dicionario["b"]
# print(meu_dicionario)

# # Reaproveitando o valor da chave excluida
# meu_dicionario = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# valor = meu_dicionario.pop("b")
# print(meu_dicionario)
# print(valor)

# # Ordenando
# dicionario = {"c": 3, "a": 1, "d": 4, "b": 2}
# chaves_ordenadas = sorted(dicionario.keys())
# print(chaves_ordenadas) 

# dicionario = {"c": 3, "a": 1, "d": 4, "b": 2}
# valores_ordenados = sorted(dicionario.values())
# print(valores_ordenados)

# Acessando elementos
#Exemplo 01
# Definindo um dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando um valor através da chave
print(pessoa["nome"]) # Saída: "João"

#Exemplo 02
# Definindo um dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando um valor com o método get()
print(pessoa.get("idade")) # Saída: 30

# Modificando um elemento
#Exemplo 01
# criação do dicionário
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# modificando um elemento
pessoa["idade"] = 30

# impressão do dicionário após a modificação
print(pessoa)

#Exemplo 02
# criação do dicionário
estoque = {
    "laranja": 10,
    "maçã": 15,
    "banana": 20
}

# modificando um elemento
estoque["banana"] = 30

# impressão do dicionário após a modificação
print(estoque)