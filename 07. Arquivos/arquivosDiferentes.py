valor_pi = 3.14159
lista_frutas = ["maçã", "banana", "laranja", "manga"]
dicionario_pessoas = {"João": 25, "Maria": 30, "Pedro": 20, "Marcos": 15}


# salvar valor_pi em um arquivo txt
with open("valor_pi.txt", "w") as f:
    f.write(str(valor_pi))

# ler valor_pi de um arquivo txt   
with open("valor_pi.txt", "r") as f:
    valor_pi_lido = f.read()
    print(f'{valor_pi_lido}, tipo {type(valor_pi_lido)}')
    

# salvar lista_frutas em um arquivo txt
with open("lista_frutas.txt", "w") as f:
    f.write(str(lista_frutas))

# ler lista_frutas de um arquivo txt
with open("lista_frutas.txt", "r") as f:
    lista_frutas_lida = f.read()
    print(f'{lista_frutas_lida}, tipo {type(lista_frutas_lida)}')
    
# salvar lista_frutas em um arquivo txt
with open("lista_frutas_split.txt", "w") as f:
    for fruta in lista_frutas:
        f.write(fruta + "\n")

# ler lista_frutas de um arquivo txt
with open("lista_frutas_split.txt", "r") as f:
    lista_frutas_lida = f.readlines()
    print(f'{lista_frutas_lida}, tipo {type(lista_frutas_lida)}')
    
    
# salvar dicionario_pessoas em um arquivo txt
with open("dicionario_pessoas.txt", "w") as f:
    f.write(str(dicionario_pessoas))

# ler dicionario_pessoas de um arquivo txt
with open("dicionario_pessoas.txt", "r") as f:
    dicionario_pessoas_lido = f.read()
    print(f'{dicionario_pessoas_lido}, tipo {type(dicionario_pessoas_lido)}')
    

#Salvando em JSON
import json

# INÍCIO DO BLOCO 1
# salvar valor_pi em um arquivo json
with open("valor_pi.json", "w") as f:
    json.dump(valor_pi, f)

# ler valor_pi de um arquivo json
with open("valor_pi.json", "r") as f:
    valor_pi_lido = json.load(f)
    print(f'{valor_pi_lido}, tipo {type(valor_pi_lido)}')
# FIM DO BLOCO 1

# INÍCIO DO BLOCO 2
# salvar lista_frutas em um arquivo json
with open("lista_frutas.json", "w") as f:
    json.dump(lista_frutas, f)

# ler lista_frutas de um arquivo json
with open("lista_frutas.json", "r") as f:
    lista_frutas_lido = json.load(f)
    print(f'{lista_frutas_lido}, tipo {type(lista_frutas_lido)}')
# FIM DO BLOCO 2

# INÍCIO DO BLOCO 3
# salvar dicionario_pessoas em um arquivo json
with open("dicionario_pessoas.json", "w") as f:
    json.dump(dicionario_pessoas, f)

# ler dicionario_pessoas de um arquivo json
with open("dicionario_pessoas.json", "r") as f:
    dicionario_pessoas_lido = json.load(f)
    print(f'{dicionario_pessoas_lido}, tipo {type(dicionario_pessoas_lido)}')
    for nome, idade in dicionario_pessoas_lido.items():
        print(nome, idade)
# FIM DO BLOCO 3

# Pickle
import pickle

# INÍCIO DO BLOCO 1
# salvar valor_pi em um arquivo pickle
with open("valor_pi.pickle", "wb") as f:
    pickle.dump(valor_pi, f)

# ler valor_pi de um arquivo pickle   
with open("valor_pi.pickle", "rb") as f:
    valor_pi_lido = pickle.load(f)
    print(f'{valor_pi_lido}, tipo {type(valor_pi_lido)}')
# FIM DO BLOCO 1

# INÍCIO DO BLOCO 2
# salvar lista_frutas em um arquivo pickle
with open("lista_frutas.pickle", "wb") as f:
    pickle.dump(lista_frutas, f)

# ler lista_frutas de um arquivo pickle
with open("lista_frutas.pickle", "rb") as f:
    lista_frutas_lida = pickle.load(f)
    print(f'{lista_frutas_lida}, tipo {type(lista_frutas_lida)}')
# FIM DO BLOCO 2

# INÍCIO DO BLOCO 3
# salvar dicionario_pessoas em um arquivo pickle
with open("dicionario_pessoas.pickle", "wb") as f:
    pickle.dump(dicionario_pessoas, f)

# ler dicionario_pessoas de um arquivo pickle
with open("dicionario_pessoas.pickle", "rb") as f:
    dicionario_pessoas_lido = pickle.load(f)
    print(f'{dicionario_pessoas_lido}, tipo {type(dicionario_pessoas_lido)}')
    for nome, idade in dicionario_pessoas_lido.items():
        print(nome, idade)
# FIM DO BLOCO 3