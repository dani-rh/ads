# # Exemplo 01 - Selecao simples
# # Recebe um número do usuário
# numero = int(input("Digite um número inteiro: "))

# # Verifica se o número é par
# if numero % 2 == 0:
#     print(f"O valor {numero} é par.")
    
# # Exemplo 02 - Selecao simples
# # Solicita as notas
# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# # Calcule a media
# media = (nota1 + nota2 + nota3 + nota4) / 4

# # Verifica se o estudante foi aprovado
# if media >= 7:
#     print("O estudante foi aprovado.")

# # Exibe a média
# print(f"A média do estudante é {media:.2f}")

# Exemplo 03 - operadores relacionais
ano_atual = 2023
nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = ano_atual - nascimento
resp = input("Voce já fez aniversário neste ano? ")

if resp == "Não":
    idade -= 1
    
print("Sua idade é",idade)
