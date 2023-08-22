''' Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes, removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.'''

frase = input("Digite um texto:")
consoantes = ""
for letra in frase:
    if letra.lower() not in "aeiou":
        consoantes = consoantes + letra

print(consoantes)