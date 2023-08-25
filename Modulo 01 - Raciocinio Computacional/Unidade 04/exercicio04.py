'''Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3, sabendo que a soma desse tipo de matriz é uma nova matriz 3x3, sendo cada elemento resultado da soma dos elementos das matrizes na mesma posição.'''

matriz1 = []
matriz2 = []
matrizSoma = []

for i in range(3):
    matriz1.append([])
    for _ in range(3):
        num = int(input("Elemento da matriz 1: "))
        matriz1[i].append(num)
for i in range(3):
    matriz2.append([])
    for _ in range(3):
        num = int(input("Elemento da matriz 2: "))
        matriz2[i].append(num)

for i in range(3):
    matrizSoma.append([])
    for j in range(3):
        num = matriz1[i][j] + matriz2[i][j]
        matrizSoma[i].append(num)

print("Matriz 1: ",matriz1)
print("Matriz 2: ",matriz2)
print("Matriz Soma: ",matrizSoma)

