notas = []
for _ in range(7):
    nota = float(input("Entre com uma das notas: "))
    notas.append(nota)
menor = min(notas)
if notas.count(menor) == 1:
    notas.remove(menor)
else:
    indice = -1
    for i in range(len(notas)):
        if notas[i] == menor:
            indice = 1
            break
    notas.pop(indice)
maior = max(notas)
if notas.count(maior) == 1:
    notas.remove(maior)
else:
    indice = -1
    for i in range(len(notas)):
        if notas[i] == maior:
            indice = i
            break
    notas.pop(indice)
soma = sum(notas)
print(f"A pontuação final do salto foi {soma: .1f}")