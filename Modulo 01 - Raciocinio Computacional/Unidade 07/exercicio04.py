'''Exercício de fixação 4: Crie um programa que leia o arquivo "alunos.txt" do exercício anterior. Em seguida, calcule a média das notas dos alunos e exiba na saída padrão. Dica: se quiser, pesquise sobre o método “split” em Python. Ele serve para dividir a string em strings menores.'''
media = 0

with open("alunos.txt", "r") as arquivo:
    notas = []
    for linha in arquivo:
        dados = linha.split(",")
        notas.append(float(dados[2]))
        
    media = sum(notas)/len(notas)
    print("A média das notas dos alunos é:", media)