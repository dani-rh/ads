# Exemplo do sistema para cadastro de clientes
import json

def menu():
    print("\nMenu:")
    print("1. Inserir clientes")
    print("2. Editar clientes")
    print("3. Listar clientes")
    print("4. Pesquisar clientes")
    print("5. Sair")
 
def inserir_cliente(nome_arquivo):
    clientes = ler_lista_do_json(nome_arquivo)
    nome = input("Insira o nome do cliente: ")
    clientes.append(nome)
    print(f"Cliente {nome} adicionado.")
    escrever_lista_em_json(clientes, nome_arquivo)
 
    return None
 
def editar_cliente(nome_arquivo):
    clientes = ler_lista_do_json(nome_arquivo)
    nome_antigo = input("Insira o nome do cliente a ser editado: ")
    if nome_antigo in clientes:
        nome_novo = input("Insira o novo nome do cliente: ")
        indice = clientes.index(nome_antigo)
        clientes[indice] = nome_novo
        print(f"Cliente {nome_antigo} alterado para {nome_novo}.")
    else:
        print("Cliente não encontrado.")
    
    escrever_lista_em_json(clientes, nome_arquivo)
    return None
 
def listar_clientes(nome_arquivo):
    clientes = ler_lista_do_json(nome_arquivo)
    print("Lista de clientes:")
    for cliente in clientes:
        print(cliente)
 
    return None
 
def pesquisar_clientes(nome_arquivo, nome):
    clientes = ler_lista_do_json(nome_arquivo)
    if nome in clientes:
        return True
    else:
        return False
 
# Funções para ler e escrever arquivos JSON
def escrever_lista_em_json(lista, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo)
        
def ler_lista_do_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return[]


arquivo = 'clientes.json' 

while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Apenas números são permitidos. Tente novamente.")
        continue
 
    if opcao == 1:
        inserir_cliente(arquivo)
    elif opcao == 2:
        editar_cliente(arquivo)
    elif opcao == 3:
        listar_clientes(arquivo)
    elif opcao == 4:
        nome = input("Insira o nome do cliente a ser pesquisado: ")
        if pesquisar_clientes(arquivo, nome):
            print(f"Cliente {nome} está na lista.")
        else:
            print("Cliente não encontrado.")
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")