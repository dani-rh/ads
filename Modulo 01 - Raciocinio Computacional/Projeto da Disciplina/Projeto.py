alunos = []

while True:
    # Mostrando o menu principal
    print("\nBem-vindo ao menu principal!\n\
1. Estudantes\n\
2. Professores\n\
3. Disciplinas\n\
4. Turmas\n\
5. Matrículas\n\
0. Sair\n ")        
    try:
        # Ler a opção escolhida pelo usuário
        opcao = int(input("Digite a opção desejada: "))
    except:
        opcao = -1
        print("Opção selecionada é inválida")
    if opcao == 1:
        print(f"Voce escolheu a opção {opcao}. Estudantes ")
        while True:
            # Mostrando o menu secundário
            print(f"\nMenu de navegação - Opção {opcao}. Estudantes\n\
1. Incluir\n\
2. Listar\n\
3. Atualizar\n\
4. Excluir\n\
5. Voltar ao menu principal\n ")
            # Ler a opcao do menu secundário
            opcao_secundaria = int(input("Digite uma opção válida: "))
            # Opção incluir/cadastrar
            if opcao_secundaria == 1:
                print(f"Opção {opcao_secundaria}. Incluir")
                codigo = int(input("Insira o código do estudante: "))
                nome = input("Insira o nome do estudante: ")
                cpf = int(input("Insira o cpf do estudante (somente números): "))
                # Dicionario com os dados dos estudantes
                dados_estudantes = {
                    "Código": codigo,
                    "Nome": nome,
                    "CPF": cpf
                }
                alunos.append(dados_estudantes)
                input("Pressione ENTER para continuar.")
            # Opção listar
            elif opcao_secundaria == 2:
                print(f"Opção {opcao_secundaria}. Listar")
                if not alunos:
                    print("Não há estudantes cadastrados")
                    input("Pressione ENTER para continuar.")
                else:
                    for nome in alunos:
                        print(nome)
                    input("Pressione ENTER para continuar.")
            # Opção atualizar/modificar
            elif opcao_secundaria == 3:
                print(f"Opção {opcao_secundaria}. Atualizar")
                codigo_editar = int(input("Qual o código do estudante que deseja editar? "))
                estudante_editar = None
                for dados_estudantes in alunos:
                    if dados_estudantes["Código"] == codigo_editar:
                        estudante_editar = dados_estudantes
                        break
                if estudante_editar is None:
                    print(f"Estudante de código {codigo_editar} não localizado na lista.")
                else:
                    estudante_editar["Código"] = int(input("Digite o novo código do estudante: "))
                    estudante_editar["Nome"] = input("Digite o novo nome do estudante: ")
                    estudante_editar["CPF"] = int(input("Digite o novo cpf do estudante: "))
                # Mostrar lista
                for estudante in alunos:
                        print(estudante)
                input("Pressione ENTER para continuar.")
            # Opção excluir
            elif opcao_secundaria == 4:
                print(f"Opção {opcao_secundaria}. Excluir")
                codigo_excluir = int(input("Qual código do estudante que deseja excluir? "))
                estudante_remover = None
                for dados_estudantes in alunos:
                    if dados_estudantes["Código"] == codigo_excluir:
                        estudante_remover = dados_estudantes
                        break
                if estudante_remover is None:
                    print(f"Estudante de código {codigo_excluir} não localizado na lista.")
                else:
                    alunos.remove(estudante_remover)
                #Mostrar lista 
                for estudante in alunos:
                        print(estudante)
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
