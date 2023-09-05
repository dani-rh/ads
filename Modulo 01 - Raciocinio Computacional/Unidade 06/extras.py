
def minhafuncao(*numeros):
    soma = 0
    par = []
    impar = []
    for i in numeros:
        soma += i
        if i % 2 == 0:
            par.append(i)
        else:
            impar.append(i)
    return soma, par, impar
  
soma, par, impar = minhafuncao(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(soma)
print(par)
print(impar)
