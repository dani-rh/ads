'''Exercício de fixação 1: Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa.'''

pessoas = []
while True:
    nome = input("Digite o nome da pessoa: ")
    rg = input("Digite o número do RG: ")
    cpf = input("Digite o número do CPF: ")
    pessoa = (nome, rg, cpf)
    pessoas.append(pessoa)
    if input("Gostaria de cadastrar mais uma pessooa (s/n): ") == "n":
        break
print(pessoas)
    
