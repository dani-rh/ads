alunos = []

while True:
    # Mostrando o menu principal
    print("Bem-vindo ao menu principal!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    # Ler a opção escolhida pelo usuário
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print(f"Voce escolheu a opção {opcao}. Estudantes ")
        while True:
                # Mostrando o menu secundário
                print(f"Menu de navegação - Opção {opcao}")
                print("1. Incluir")
                print("2. Listar")
                print("3. Atualizar")
                print("4. Excluir")
                print("5. Voltar ao menu principal")

                # Ler a opcao do menu secundário
                opcao_secundaria = int(input("Digite uma opção válida: "))
                if opcao_secundaria == 1:
                    print(f"Opção {opcao_secundaria}. Incluir")
                    nome = input("Insira o nome do aluno: ")
                    alunos.append(nome)
                    input("Pressione ENTER para continuar.")
                elif opcao_secundaria == 2:
                    print(f"Opção {opcao_secundaria}. Listar")
                    if not alunos:
                        print("Não há estudantes cadastrados")
                        input("Pressione ENTER para continuar.")
                    else:
                        for nome in alunos:
                            print(nome)
                        input("Pressione ENTER para continuar.")
                elif opcao_secundaria == 3:
                    print(f"Opção {opcao_secundaria}. Atualizar")
                    print("EM DESENVOLVIMENTO")
                    input("Pressione ENTER para continuar.")
                elif opcao_secundaria == 4:
                    print(f"Opção {opcao_secundaria}. Excluir")
                    print("EM DESENVOLVIMENTO")
                    input("Pressione ENTER para continuar.")
                elif opcao_secundaria == 5:
                    break
                else:
                    print("Voce escolheu uma opção secundária inválida.")
            
    elif opcao == 2:
        print(f"Voce escolheu a opção {opcao}. Professores ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif opcao == 3:
        print(f"Voce escolheu a opção {opcao}. Disciplinas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif opcao == 4:
        print(f"Voce escolheu a opção {opcao}. Turmas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif opcao == 5:
        print(f"Voce escolheu a opção {opcao}. Matriculas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif opcao == 0:
        print("Programa encerrado.")
        break
    else:
        print("Voce escolheu uma opção inválida.")
        





