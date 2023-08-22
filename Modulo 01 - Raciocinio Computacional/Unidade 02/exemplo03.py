# Exemplo 03 - operadores relacionais
ano_atual = 2023
nascimento = int(input("Qual é o seu ano de nascimento? "))
idade = ano_atual - nascimento
resp = input("Voce já fez aniversário neste ano? ")

if resp == "Não":
    idade -= 1
    
print("Sua idade é",idade)