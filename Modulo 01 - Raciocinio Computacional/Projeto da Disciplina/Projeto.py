# Mostrando o menu principal
print("Bem-vindo ao menu!")
print("1. Estudantes")
print("2. Professores")
print("3. Disciplinas")
print("4. Turmas")
print("5. Matrículas")
print("0. Sair")

# Ler a opção escolhida pelo usuário
opcao = int(input("Digite uma opção: "))

if opcao > 0 and opcao <= 5:
    print(f"Voce escolheu a opção {opcao}")
    
    # Mostrando o menu secundário
    print(f"Menu de navegação - Opção {opcao}")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")

    # Ler a opcao do menu secundário
    opcao_secundaria = int(input("Digite uma opção válida: "))
    if opcao_secundaria >= 0 and opcao_secundaria <= 5:
        print(f"Voce escolheu a opção {opcao_secundaria}")
    else:
        print("Voce escolheu uma opção secundária inválida.")
elif opcao == 0:
    print("Voce pediu para sair.")

else:
        print("Voce escolheu uma opção inválida.")





