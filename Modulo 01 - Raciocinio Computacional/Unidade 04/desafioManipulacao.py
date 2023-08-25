numeros = list(range(-10,11))
imparesNegativos = []
paresPositivos = []

for item in list(numeros):
    if item % 2 == 0 and item > 0:
        paresPositivos.append(item)
    elif item % 2 == 1 and item < 0:
        imparesNegativos.append(item)

print(numeros)
print(paresPositivos)
print(imparesNegativos)

# Solução professor:
positivos_pares = []
negativos_impares = []

for i, num in enumerate(range(-10,11)):
    if num < 0:
        if num % 2 == 1:
            negativos_impares.append([i,num])
    else:
        if num % 2 == 0:
            positivos_pares.append([i,num])
            
print("Números Negativos Impares:")
for i in negativos_impares:
    print(i)
print("Números Positivos Pares:")
for i in positivos_pares:
    print(i)