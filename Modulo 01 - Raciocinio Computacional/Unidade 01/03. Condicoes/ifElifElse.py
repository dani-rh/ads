# Caso 01
# nota1 = float(input("Digite a nota da primeira prova: "))
# nota2 = float(input("Digite a nota da segunda prova: "))
# media = (nota1 + nota2) / 2.0

# if media >= 7:
#     print("Parabéns, voce foi aprovado com média",media)
#     print("Continue estudando e se preparando para os próximos desafios.")
# elif media >= 5:
#     print("Voce está em recuperação com média",media)
#     print("Voce precisa estudar mais para a próxima prova.")
# else:
#     print("Infelizmente, voce foi reprovado com média",media)    
#     print("Voce precisa estudar mais para a próxima oportunidade.")
    
    
# Caso 02 - Tres elifs

# nota1 = float(input("Digite a nota da primeira prova: "))
# nota2 = float(input("Digite a nota da segunda prova: "))
# media = (nota1 + nota2) / 2.0

# if media >= 9.5:
#     print("Parabéns, a sua nota foi excelente! Você foi aprovado com média", media)
# elif media >= 8:
#     print("Parabéns, a sua nota foi muito boa! Você foi aprovado com média", media)
# elif media >= 7:
#     print("Parabéns, você foi aprovado com média", media)
#     print("Continue estudando e se preparando para os próximos desafios.")
# elif media >= 5:
#     print("Você está em recuperação com média", media)
#     print("Você precisa estudar mais para a próxima prova.")
# else:
#     print("Infelizmente, você foi reprovado com média", media)
#     print("Você precisa estudar mais para a próxima oportunidade.")
    
# # if dentro de if

# idade = int(input("Qual é a sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade.")
#     if idade >= 21:
#         print("Você pode beber nos Estados Unidos.")
# else:
#     print("Você é menor de idade.")

# if dentro de if dentro de if

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

if nota1 >= 7:
    if nota2 >= 7:
        if nota3 >= 7:
            print("Parabéns, você foi aprovado(a)!")
        else:
            print("Sua nota na terceira avaliação foi abaixo da média.")
    else:
        print("Sua nota na segunda avaliação foi abaixo da média.")
else:
    print("Sua nota na primeira avaliação foi abaixo da média.")