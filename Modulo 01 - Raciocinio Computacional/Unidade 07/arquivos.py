# Exemplo escrita em arquivo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Counter-Strike é melhor do que Valorant.")
    arquivo.write("O correto é 'bolacha'.")
    
# Exemplo leitura em arquivo
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)