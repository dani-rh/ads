'''A partir do exercício 2 e após mostrar o resultado na tela, peça novamente para que o usuário digite uma nova frase. Adicione esta nova frase no mesmo arquivo de texto sem apagar o conteúdo que já estava lá, e mostre o resultado na tela.'''

# pede a frase
frase = input("Digite uma frase: ")

# salva a frase em um arquivo de texto
with open("frase.txt", "w") as arquivo:
    arquivo.write(frase + "\n")
    
# abre o arquivo e exibe na tela
with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
    
# pede outra frase
frase = input("Digite uma frase: ")

# abre o arquivo em modo "a"e adiciona a nova frase
with open("frase.txt", "a") as arquivo:
    #adiciona a nova frase:
    arquivo.write(frase + "\n")
    
# abre o arquivo e exibe na tela
with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)