agenda = {}
print("*** Cadastro de telefones ***")
while True:
    contato = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já cadastrado com o número {agenda[contato]}. Deseja alterar? (s/n)") == "n":
            continue
    if telefone in agenda.values():
        print("Telefone já cadastrado para outro contato.")
        continue
    agenda[contato] = telefone # add o telefone no dic agenda, a chave para encontrarmos o telefone será o contato
    if input("Deseja cadastrar um novo contato (s/n): ") == "n":
        break
print(agenda)