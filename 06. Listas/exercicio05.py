'''Crie um dicionário com o nome e a profissão de duas pessoas e adicione uma terceira pessoa com nome e profissão.'''

pessoas = {
    "nome" : "Daniela",
    "profissão" : "Desenvolvedora"
}
print(pessoas)

nome = input("Digite o nome da segunda pessoa: ")
profissao = input("Digite a profissão segunda pessoa: ")
pessoas[nome] = profissao
    
print(pessoas)

#adiciona a terceira pessoa
nome = input("Digite o nome da terceira pessoa: ")
profissao = input("Digite a profissão da terceira pessoa: ")
pessoas[nome] = profissao

print(pessoas)