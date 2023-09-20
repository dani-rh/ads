import json

# Dicionário nomes menu principal
nomes_menu_principal = {
    1: "Estudantes",
    2: "Professores",
    3: "Disciplinas",
    4: "Turmas",
    5: "Matrículas"
}

# Dicionário de campos para cada tipo de cadastro
campos_cadastro = {
    "estudantes.json": ["Código", "Nome", "CPF"],
    "professores.json": ["Código", "Nome", "CPF"],
    "disciplinas.json": ["Código", "Nome"],
    "turmas.json": ["Código", "Código do professor", "Código da disciplina"],
    "matriculas.json": ["Código da turma", "Código do estudante"]
}

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
    nome_menu = nomes_menu_principal.get(menu)
    print(f"\nMenu de navegação - Opção {menu}. {nome_menu}\n\
1. Incluir\n\
2. Listar\n\
3. Atualizar\n\
4. Excluir\n\
5. Voltar ao menu principal\n ")
    return int(input("Escolha uma operação: "))

# Função validar CPF
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True

# Função cadastrar estudante ou professor
def cadastrar(nome_arquivo):
    lista_cadastro = ler_json(nome_arquivo)
    novo_cadastro = {}
    
    for campo in campos_cadastro[nome_arquivo]:
        while True:
            valor = input(f"Insira o {campo}: ")
            
            if "Código" in campo:
                try:
                    valor = int(valor)
                    if any(cadastro.get(campo) == valor for cadastro in lista_cadastro):
                        print(f"{campo} já cadastrado. Por favor, insira um novo {campo}.")
                        continue
                    novo_cadastro[campo] = valor
                    break
                except ValueError:
                    print(f"{campo} deve ser um número e não pode ficar vazio.")
            elif campo == "CPF" and nome_arquivo in ["estudantes.json", "professores.json"]:
                if not validar_cpf(valor) or any(pessoa.get(campo) == valor for pessoa in lista_cadastro):
                    if any(pessoa[campo] == valor for pessoa in lista_cadastro):
                        print("CPF já cadastrado. Por favor, insira um novo CPF.")
                    else:
                        print("CPF deve conter 11 dígitos e apenas números.")
                    continue
                else:
                    novo_cadastro[campo] = int(valor)
                    break
            else:    
                if valor:
                    if campo == "Nome" and not valor.isalpha():
                        print(f"{campo} deve conter apenas letras.")
                        continue
                    novo_cadastro[campo] = valor
                    break
                print(f"{campo} não pode ficar vazio.")
        
    lista_cadastro.append(novo_cadastro)
    salvar_json(lista_cadastro, nome_arquivo)
    
# Função listar 
def listar_cadastro(nome_arquivo):
    lista_cadastro = ler_json(nome_arquivo)
    if not lista_cadastro:
        print("Não há cadastros salvos no arquivo")
    else:
        for cadastro in lista_cadastro:
            print(f"Dados: {cadastro}")

# Função editar/atualizar 
def editar_cadastro(codigo_editar, nome_arquivo):
    lista_cadastro = ler_json(nome_arquivo)
    cadastro_editar = None
    for dados_cadastro in lista_cadastro:
        if dados_cadastro.get("Código") == codigo_editar:
            cadastro_editar = dados_cadastro
            break
    if cadastro_editar is None:
        print(f"Código {codigo_editar} não localizado na lista.")
        return
    
    for campo in campos_cadastro[nome_arquivo]:
        while True:
            valor = input(f"Digite o novo {campo}: ")
            
            #Validar CPF estudantes e professores:
            if campo == "CPF" and nome_arquivo in["estudantes.json", "professores.json"]:
                while not validar_cpf(valor) or (valor != cadastro_editar["CPF"] and any(pessoa.get(campo) == valor for pessoa in lista_cadastro)):
                    if any(pessoa[campo] == valor for pessoa in lista_cadastro):
                        print("CPF já cadastrado. Por favor, insira um novo CPF")
                    else:
                        print("CPF deve conter 11 dígitos e apenas números.")
                    valor = input(f"Digite o novo {campo}: ")
                cadastro_editar[campo] = int(valor) if valor.isdigit() else valor
                break
            # Validar código
            elif "Código" in campo:
                while valor != cadastro_editar[campo] and any(cadastro.get(campo) == int(valor) for cadastro in lista_cadastro):
                    print(f"{campo} já cadastrado. Por favor, insira um novo {campo}.")
                    valor = input(f"Digite o novo {campo}: ")
                cadastro_editar[campo] = int(valor) if valor.isdigit() else valor
                break
        
            else:
                if valor:
                    cadastro_editar[campo] = int(valor) if valor.isdigit() else valor
                    break
                print(f"{campo} não pode ficar vazio.")
      
    salvar_json(lista_cadastro, nome_arquivo)
    
# Função excluir
def excluir_cadastro(codigo_excluir, nome_arquivo):
    cadastro_remover = None
    lista_cadastro = ler_json(nome_arquivo)
    for cadastro in lista_cadastro:
        if cadastro["Código"] == codigo_excluir:
            cadastro_remover = cadastro
            break
    if cadastro_remover is None:
        print(f"Código {codigo_excluir} não localizado na lista.")
    else:
        lista_cadastro.remove(cadastro_remover)
        salvar_json(lista_cadastro, nome_arquivo)
        
# Função mostrar lista 
def mostrar_lista(nome_arquivo):
    lista_estudante = ler_json(nome_arquivo)
    for estudante in lista_estudante:
        print(estudante)

# Função escrever lista em json
def salvar_json(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
    # with open('alunos.json', "w") as arquivo:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)
        
# Função ler lista em json
def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
            return lista
    except FileNotFoundError:
        return []  
    
def processar_menu_operacoes(operacao, nome_arquivo):
    if operacao == 1:
        print(f"Opção {operacao}. Incluir")
        cadastrar(nome_arquivo)
        input("Pressione ENTER para continuar.")
# Opção listar
    elif operacao == 2:
        print(f"Opção {operacao}. Listar")
        listar_cadastro(nome_arquivo)
        input("Pressione ENTER para continuar.")
# Opção atualizar/modificar
    elif operacao == 3:
        print(f"Opção {operacao}. Atualizar")
        codigo_editar = int(input("Qual o código do cadastro que deseja editar? "))
        editar_cadastro(codigo_editar, nome_arquivo)
    # Mostrar lista 
        mostrar_lista(nome_arquivo)
        input("Pressione ENTER para continuar.")
# Opção excluir
    elif operacao == 4:
        print(f"Opção {operacao}. Excluir")
        codigo_excluir = int(input("Qual código do cadastro que deseja excluir? "))
        excluir_cadastro(codigo_excluir, nome_arquivo)
    #Mostrar lista 
        mostrar_lista(nome_arquivo)
        input("Pressione ENTER para continuar.")
    elif operacao == 5:
        return False
    else:
        print("Voce escolheu uma opção secundária inválida.")
    
    return True


arquivo_estudante = "estudantes.json"
arquivo_professor = "professores.json"
arquivo_disciplina = "disciplinas.json"
arquivo_turma = "turmas.json"
arquivo_matricula = "matriculas.json"


while True:
    # Mostrando o menu principal e lendo a opcao escolhida
    menu = mostrar_menu_principal()        
    print(f"Você escolheu a opção ",menu)
    if menu == 1:
        while True:
            operacao = mostrar_menu_secundario(menu)
            if not processar_menu_operacoes(operacao, arquivo_estudante):
                break     
    elif menu == 2:
        while True:
            operacao = mostrar_menu_secundario(menu)
            if not processar_menu_operacoes(operacao, arquivo_professor):
                break
    elif menu == 3:
        while True:
            operacao = mostrar_menu_secundario(menu)
            if not processar_menu_operacoes(operacao, arquivo_disciplina):
                break
    elif menu == 4:
        while True:
            operacao = mostrar_menu_secundario(menu)
            if not processar_menu_operacoes(operacao, arquivo_turma):
                break
    elif menu == 5:
        while True:
            operacao = mostrar_menu_secundario(menu)
            if not processar_menu_operacoes(operacao, arquivo_matricula):
                break
    elif menu == 0:
        print("Programa encerrado!")
        break
    else:
        print("Voce escolheu uma opção inválida.")
