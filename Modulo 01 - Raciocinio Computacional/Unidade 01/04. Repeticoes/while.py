# i = 1
# while i <= 100:
#     print(i)
#     i += 1   
    
# # Soma de 1 a 10
# i = 1
# soma = 0
# while i <= 10:
#     soma += i
#     print(soma) 
    
#     i += 1
    
# # Testando uma senha
# senha = ""
# while senha != "12345":
#     senha = input("Digite a senha: ")
# print("Acesso permitido!")

# # Menu
# opcao = ''
# while opcao != 's':
#     print("MENU")
#     print("a. Opção 1")
#     print("b. Opção 2")
#     print("c. Opção 3")
#     print("s. Sair")
#     opcao = input("Digite uma opção: ")
#     if opcao == 'a':
#         print("Opção 1 selecionada")
#     elif opcao == 'b':
#         print("Opção 2 selecionada")
#     elif opcao == 'c':
#         print("Opção 3 selecionada")
#     elif opcao == 's':
#         print("Saindo...")
#     else:
#         print("Opção inválida.")
        
# # Testando números
# num = int(input("Digite um número (digite 0 para sair):"))
# while num != 0:
#     if num > 0:
#         print("O número é positivo")
#     else:
#         print("O número é negativo")
#     num = int(input("DIgite outro número (digite 0 para sair): "))

# Inserindo notas
nota = -1
while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))
print("Nota válida: ",nota)

