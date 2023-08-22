'''Crie um código que peça para o usuário digitar uma frase. Salve o resultado em uma arquivo de texto. Depois, abra este arquivo de texto que salvou e mostre o resultado na tela.'''

# pede a frase
frase = input("Digite uma frase: ")

# salva a frase em um arquivo de texto
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase)
    
# abre o arquivo e exibe na tela
with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)