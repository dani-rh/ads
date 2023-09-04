def nomedafuncao(*args):
    print(args[0])
    print(args[1])
    
def somar(*numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

resultado = somar(2, 3, 4, 5, 8)
print(f"A soma dos números é {resultado}")