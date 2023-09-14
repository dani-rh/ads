nome = input("Digite o seu nome: ")

with open("nome.txt", "w") as f:
    f.write(nome)