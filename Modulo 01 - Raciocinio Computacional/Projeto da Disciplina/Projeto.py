# Funções
# Mostrar menu principal
def mostrar_menu_principal():
        print("\nBem-vindo ao menu principal!\n\
1. Estudantes\n\
2. Professores\n\
3. Disciplinas\n\
4. Turmas\n\
5. Matrículas\n\
0. Sair\n ") 
        return int(input("Digite a opção desejada: "))
        
# Mostrar menu secundario
def mostrar_menu_secundario(menu):
    print(f"\nMenu de navegação - Opção {menu}. Estudantes\n\
1. Incluir\n\
2. Listar\n\
3. Atualizar\n\
4. Excluir\n\
5. Voltar ao menu principal\n ")
    return int(input("Escolha uma operação: "))

# Função cadastrar estudante
def cadastrar_estudante(dados_estudantes):
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

# Função listar estudante
def listar_estudante():
    for nome in alunos:
        print(nome)

# Função editar/atualizar estudante
def editar_estudante():
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

# Função excluir
def excluir_estudante():
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

alunos = []

while True:
    # Mostrando o menu principal e lendo a opcao escolhida
    menu = mostrar_menu_principal()        
    print(f"Você escolheu a opção ",menu)
    if menu == 1:
        while True:
        # Mostrando o menu secundário e lendo a opcao escolhida
            operacao = mostrar_menu_secundario(menu)
        # Opção incluir/cadastrar
            if operacao == 1:
                print(f"Opção {operacao}. Incluir")
                cadastrar_estudante(alunos)
                input("Pressione ENTER para continuar.")
        # Opção listar
            elif operacao == 2:
                print(f"Opção {operacao}. Listar")
                if not alunos:
                    print("Não há estudantes cadastrados")
                    input("Pressione ENTER para continuar.")
                else:
                    listar_estudante()
                    input("Pressione ENTER para continuar.")
        # Opção atualizar/modificar
            elif operacao == 3:
                print(f"Opção {operacao}. Atualizar")
                editar_estudante()
            # Mostrar lista
                for estudante in alunos:
                        print(estudante)
                input("Pressione ENTER para continuar.")
        # Opção excluir
            elif operacao == 4:
                print(f"Opção {operacao}. Excluir")
                excluir_estudante()
            #Mostrar lista 
                for estudante in alunos:
                        print(estudante)
                input("Pressione ENTER para continuar.")
            elif operacao == 5:
                break
            else:
                print("Voce escolheu uma opção secundária inválida.")
    elif menu == 2:
        print(f"Voce escolheu a opção {menu}. Professores ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif menu == 3:
        print(f"Voce escolheu a opção {menu}. Disciplinas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif menu == 4:
        print(f"Voce escolheu a opção {menu}. Turmas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif menu == 5:
        print(f"Voce escolheu a opção {menu}. Matriculas ")
        print("EM DESENVOLVIMENTO")
        input("Pressione ENTER para continuar.")
    elif menu == 0:
        print("Programa encerrado.")
        break
    else:
        print("Voce escolheu uma opção inválida.")
