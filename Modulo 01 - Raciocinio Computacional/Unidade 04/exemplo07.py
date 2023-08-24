nomes = []
while True:
    nome = input("Digite o nome: ")
    if nome == "sair":
        break
    sobrenome = input("Digite o sobrenome: ")
    nome_completo = [nome, sobrenome]
    nomes.append(nome_completo)
    
for nome in nomes:
    print(nome[1] + ", "+ nome[0])