'''Crie um programa que peça para o usuário inserir um login e uma senha. Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações. Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".'''

while True:
    login = input("Digite um login: ")
    senha = input("Digite uma senha: ")
    if login == senha:
        print("Dados inválidos. Por favor, insira novamente.")
    else:
        break
print("Bem-vindo ao sistema!")
    