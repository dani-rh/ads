'''Escreva um código que solicite a idade e o gênero de uma pessoa e informe se ela pode se aposentar, levando em consideração as seguintes regras: mulheres podem se aposentar com 63 anos ou mais, enquanto homens podem se aposentar com 68 anos ou mais.'''

idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu genero: ")

if idade >= 63 and genero == "F":
    print("Pode se aposentar")
elif genero == "M" and idade >= 68:
    print("Pode se aposentar!")
else:
    print("Voce ainda não pode se aposentar.")    

