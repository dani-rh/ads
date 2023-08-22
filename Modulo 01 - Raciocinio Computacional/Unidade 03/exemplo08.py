while True:
    try:
        num = float(input("Digite um número decimal: "))
        break
    except ValueError:
        print("Valor inválido")
print("Número validado: ",num)