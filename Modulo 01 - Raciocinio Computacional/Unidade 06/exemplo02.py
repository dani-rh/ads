# agenda_telefonica = {}

# def inserir(nome, telefone, agenda):
#     if nome in agenda:
#         if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
#             return False
#     agenda[nome] = telefone
#     return True

# while True:
#     nome = input("Digite o nome do contato: ")
#     telefone = input("Digite o telefone do contato: ")
#     if inserir(nome, telefone, agenda_telefonica):
#         print("Contato adicionado ou atualizado com sucesso!")
#     else:
#         print("Falha ao tentar adicionar o contato!")
#     if input("Gostaria de adicionar um novo contato? (s/n) ") == "n":
#         break
    
# print(agenda_telefonica)

# Exemplo com valor padrão
agenda_telefonica = {}

def inserir(nome, agenda, telefone = "Sem telefone"):
    if nome in agenda:
        if input("Contato já cadastrado. Deseja alterar o telefone? (s/n) ") == "n":
            return False
    agenda[nome] = telefone
    return True

inserir("Fulano", agenda_telefonica)
inserir("Beltrano", agenda_telefonica, 1232231413)

print(agenda_telefonica)