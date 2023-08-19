# elementos = [5, 900, 1, -2]
# print(f'Os elementos invertidos são {reversed(elementos)}.')
# print(f'Os elementos invertidos são {list(reversed(elementos))}.')
# print(f'Os elementos ordenados são {sorted(elementos)}.')

# print('\nUsando loop para mostrar os elementos invertidos:')
# for i in reversed(elementos):
#     print(i)

# print('\nUsando loop para mostrar os elementos ordenados:')
# for i in sorted(elementos):
#     print(i)

# # Criando função
# def saudar_usuario():
#     print("Olá! Tudo bem por aí?")
    
# saudar_usuario()
# saudar_usuario()
# saudar_usuario()
# saudar_usuario()
# saudar_usuario()
    
# # Exemplo
# def somar(a,b):
#     resultado = a + b
#     return resultado

# soma = somar(2,5)
# print(soma)

# soma = somar(5,2)
# print(soma)

# soma = somar(1000, -20)
# print(soma)

# # Exemplo com fatorial

# def calcular_fatorial(numero):
#     fatorial = 1
#     for i in range(1, numero+1):
#         fatorial *= i
#     return fatorial

# a = 5
# resultado = calcular_fatorial(a)
# print(resultado)

# b = 3
# resultado = calcular_fatorial(b)
# print(resultado)

# # Exemplo com dois parametros
# def calcular_area_triangulo (base, altura):
#     area = (base * altura) / 2
#     return area

# resultado = calcular_area_triangulo(10, 5)
# print(resultado)

# # Exemplo com condicao
# def eh_par(numero):
#     if numero % 2 == 0:
#         return True
#     else:
#         return False

# resultado = eh_par(10)
# print(resultado)

# # Exemplo retornando dois valores
# def calcular_areas(base, altura):
#     area_triangulo = (base * altura) / 2
#     area_retangulo = base * altura
#     return area_triangulo, area_retangulo

# triangulo, retangulo = calcular_areas(10, 5)
# print(f"A área do retangulo é {retangulo}")
# print(f"A área do triangulo é {triangulo}")

# # Funcao sem parametros e com retorno
# def mostrar_nome_idade_exemplo():
#     return "Fulano de Tal", 42

# nome, idade = mostrar_nome_idade_exemplo()
# print(nome, idade)

# # Funcao com parametros e sem retorno
# def eh_par(numero):
#     if numero % 2 == 0:
#         print(numero, "é um número par")
#     else:
#         print(numero,"não é um número par")
        
# eh_par(10)

# Funcao sem parametros e sem retorno
def mostrar_menu():
    print("Olá! Digite uma opção do menu. Em seguida, aperte Enter.")
    print("1 - Listar todos os cadastros.")
    print("2 - Fazer um novo cadastro.")
    print("3 - Remover um cadastro já existente.")
    print("4 - Modificar um cadastro já existente.")
    print("9 - Ajuda.")
    print("0 - Sair.")
    
mostrar_menu()