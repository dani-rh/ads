'''Modifique o código do exercício 4 para que salve, dentro de um único arquivo, as duas listas. Depois, abra novamente o arquivo pickle que salvou e mostre na tela o seu conteúdo.'''

import pickle
# cria a lista
numeros = list(range(1,11))

# filtra os numeros pares
numeros_pares = []
for num in numeros:
    if num % 2 == 0:
        numeros_pares.append(num)
        
#salva a lista de numeros pares em um arquivo pickle
with open("numeros_pares.pickle", "wb") as f:
    pickle.dump([numeros, numeros_pares], f)
    
#abre o arquivo  pickle e mostra na tela
with open("numeros_pares.pickle", "rb") as f:
    numeros_lidos, numeros_pares_lidos = pickle.load(f)
    print(numeros_lidos)
    print(numeros_pares_lidos)