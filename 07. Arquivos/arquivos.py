# Criando
with open("receita.txt", "w") as f:
    f.write("Bolo de chocolate\n")
    f.write("Ingredientes:\n")
    f.write("- 2 xícaras de açúcar\n")
    f.write("- 1 e 3/4 xícaras de farinha de trigo\n")
    f.write("- 3/4 xícara de cacau em pó\n")
    
print("Finalizou!")

# Lendo
with open("receita.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)

# Lendo 2 (sem usar o with)
f = open("receita.txt", "r")
conteudo = f.read()
print(conteudo)
f.close()

with open("receita.txt", "a") as f:
    f.write("- 1 colher de sopa de fermento em pó\n")
    f.write("- Granulado a gosto\n")