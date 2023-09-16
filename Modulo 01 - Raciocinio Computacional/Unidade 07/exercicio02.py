'''Exercício de fixação 2: Crie um programa que leia o arquivo “números.txt” do exercício anterior, e calcule a soma desses números.'''
soma = 0

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        soma += int(linha)
        
print(soma)