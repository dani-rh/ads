'''Exercício de fixação 6: Crie um programa que, fazendo uso de funções, cadastre contatos em uma agenda telefônica, podendo exclui-los. Deve ser exibido um menu com as opções: inserir, remover e sair.'''

def dados_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    return nome, telefone

def inserir(agenda):
    contato = dados_contato()
    if contato[0] in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            return False
    agenda[contato[0]] = contato[1]
    return True

def remover(nome, agenda):
    if nome in agenda:
        del agenda[nome]
        return True
    else:
        return False
    
def menu():
    print("*** Agenda Telefonica ***")
    print("1. Inserir contato")
    print("2. Remover contato")
    print("3. Sair")
    return int(input("Escolha uma das opções: "))



agenda_telefonica = {}
while True:
    op = menu()
    if op == 1:
        if inserir(agenda_telefonica):
            print("Contato cadastrado com sucesso")
            print(agenda_telefonica)
        else:
            print("Operação não realizada")
    elif op == 2:
        nome = input("Digite o nome do contato a ser removido: ")
        if remover(nome, agenda_telefonica):
            print("Contato removido com sucesso")
            print(agenda_telefonica)
        else:
            print("Operação não realizada")
    else:
        break