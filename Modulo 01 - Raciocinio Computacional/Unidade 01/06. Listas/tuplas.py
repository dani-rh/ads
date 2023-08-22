# Criando tuplas
coordenadas = (40.7128, -74.0060)
dias_da_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
pontuacao_jogo = (1200, 3)
print(coordenadas)
print(dias_da_semana)
print(pontuacao_jogo)

# Percorrendo tuplas
animais = ("gato", "cachorro", "papagaio", "peixe")

for animal in animais:
    print(animal)

# Localizando um elemento
carros = ("fusca", "fiesta", "oggi", "uno")

if "fusca" in carros:
    print("O fusca está na lista")
else:
    print("O fusca não está na lista")
    
# Adicionando ou removendo elementos
tupla1 = (1, 2, 3)
tupla2 = tupla1 + (4,)
print(tupla2)  # saída: (1, 2, 3, 4)

# Ordenando
numeros = (5, 1, 3, 2, 4)
numeros_ordenados = tuple(sorted(numeros))
print(numeros_ordenados) # saída: (1, 2, 3, 4, 5)

nomes = ("Ana", "Carlos", "Beatriz", "Daniel")
nomes_ordenados = tuple(sorted(nomes))
print(nomes_ordenados) # saída: ('Ana', 'Beatriz', 'Carlos', 'Daniel')

# Acessando elementos
tupla = ('a', 'b', 'c', 'd', 'e')
elemento = tupla[2]
print(elemento) 

tupla = ('a', 'b', 'c', 'd', 'e')
subtupla = tupla[1:4]
print(subtupla)

