lista_vazia = []
print(lista_vazia)

lista_vazia.append(10)
lista_vazia.append(20)
lista_vazia.append(30)
print(lista_vazia)

# Percorrendo listas
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta)
    
# Adicionando elementos
numeros = [1, 2, 3, 4]
numeros.append(5)
print(numeros)

# Removendo elementos
paises = ["Brasil", "EUA", "Japão", "Alemanha"]
print(paises)
paises.remove("Japão")
print(paises)

# Ordenando elementos
# Ordem crescente
numeros = [3, 1, 4, 2, 5]
numeros.sort()
print(numeros)
# Ordem decrescente
numeros = [3, 1, 4, 2, 5]
numeros.sort(reverse=True)
print(numeros)

# Acessando elementos
frutas = ["maçã", "banana", "laranja", "uva"]
print(frutas[0]) # imprime "maçã"
print(frutas[2]) # imprime "laranja"

# Modificando elementos
lista = [1, 2, 3, 4, 5]
lista[2] = 10
print(lista)