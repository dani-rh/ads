idade = int(input("Qual é a sua idade? "))

# Primeiro bloco de if/else
if idade < 18:
    print("Você é menor de idade!")
else:
    print("Você é maior de idade!")

# Segundo bloco de if/elif/else
media = float(input("Qual é a sua média na disciplina? "))

if media >= 7:
    print("Parabéns, você foi aprovado com média", media)
    print("Continue estudando e se preparando para os próximos desafios.")
elif media >= 5:
    print("Você está em recuperação com média", media)
    print("Você precisa estudar mais para a próxima prova.")
else:
    print("Infelizmente, você foi reprovado com média", media)
    print("Você precisa estudar mais para a próxima oportunidade.")

# Terceiro bloco de if/else
saldo = float(input("Qual é o seu saldo na conta-corrente? "))

if saldo < 0:
    print("O seu saldo está negativo!")
elif saldo == 0:
    print("O seu saldo está zerado!")
else:
    print("O seu saldo está positivo!")