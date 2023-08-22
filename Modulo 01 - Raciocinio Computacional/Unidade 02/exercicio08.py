'''Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria e o número de faltas. Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:'''

nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
nota3 = float(input("Informe a terceira nota:"))
nota4 = float(input("Informe a quarta nota:"))
faltas = int(input("Informe o número de faltas:"))

media = (nota1 + nota2 + nota3 + nota4) / 4
print("Sua média na disciplina foi",media)

presenca = 100 - (faltas*100) /40
print("Sua porcentagem de presença é de",presenca)

if media >= 7 and presenca >= 75:
    print("Voce está aprovado na disciplina!")
elif media >= 7 and presenca < 75:
    print("Voce foi reprovado por faltas!")
elif media < 7 and presenca >= 75:
    print("Voce foi reprovado por nota!")
else:
    print("Voce foi reprovado por nota e por faltas!")
