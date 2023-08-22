while True:
    try:
        num = int(input("Digite um número: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado: ", num)
