'''Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10'''

num = int(input("Digite um número: "))
print("Tabuada do", num)
for i in range (1,11):
    mult = i * num
    print(i, "x", num, "=", mult)