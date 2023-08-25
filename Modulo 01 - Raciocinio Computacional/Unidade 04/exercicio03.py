'''Crie um programa que leia as temperaturas médias de cada mês do ano e as armazene em uma lista; use outro vetor para guardar e exibir, quando necessário, o nome dos meses do ano; calcule a média anual de temperatura e informe quais meses ficaram acima da média anual.'''

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperaturas = []
soma = 0
for mes in meses:
    temperatura = float(input("Temperatura média em " + mes + ": "))
    temperaturas.append(temperatura)
    soma += temperatura
    
media = soma / 12
print(f"Meses com temperatura acima da média de {media:.1f} graus")
for i in range(12):
    if temperaturas[i] > media:
        print(f"{meses[i]}:{temperaturas[i]:.1f} graus")