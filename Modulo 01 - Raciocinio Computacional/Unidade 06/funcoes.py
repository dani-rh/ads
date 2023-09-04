# def calcular_imc(lista_de_pessoas):
#     for pessoa in lista_de_pessoas:
#         altura = pessoa['altura']
#         peso = pessoa['peso']
#         imc = peso / (altura ** 2)
#         print(f'O IMC de {pessoa["nome"]} é {imc:.2f}')

# # Dados das pessoas em formato de lista de dicionários 
# pessoas = [
#      {'nome': 'João', 'altura': 1.75, 'peso': 70},
#     {'nome': 'Maria', 'altura': 1.60, 'peso': 55},
#     {'nome': 'Carlos', 'altura': 1.80, 'peso': 90}
# ]
# # Cálculo do IMC para cada pessoa
# calcular_imc(pessoas)    

# print("Continuando o calculo para uma nova lista de pessoas.")
# print("Este aqui é só um print para demonstrar o código.")

# # Dados das pessoas em formato de lista de dicionários
# novas_pessoas = [
#     {'nome': 'Cézar', 'altura': 1.78, 'peso': 79},
#     {'nome': 'Marta', 'altura': 1.61, 'peso': 52},
#     {'nome': 'Ana', 'altura': 1.65, 'peso': 70}
# ]

# # Cálculo do IMC para cada pessoa
# calcular_imc(novas_pessoas)

# print("Agora, vamos para a lista final.")

# # Dados das pessoas em formato de lista de dicionários
# mais_pessoas = [
#     {'nome': 'Kauane', 'altura': 1.53, 'peso': 51}
# ]
# # Cálculo do IMC para cada pessoa
# calcular_imc(mais_pessoas)

#Função com parâmetros e com retorno:
def soma_tres_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_tres_numeros(5, 10, 2))

#Função com parâmetros e sem retorno:
def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")

saudacao_personalizada("Fulano")

# Função sem parâmetros e com retorno:
def get_numero_pi():
    return 3.141592653589793

print(f"O valor de pi é {get_numero_pi()}.")
print(f"O valor de pi é {get_numero_pi()}.")
print(f"O valor de pi é {get_numero_pi()}.")

# Função sem parâmetros e sem retorno:
def saudacao():
    print("Olá, mundo!")

saudacao()
saudacao()
saudacao()