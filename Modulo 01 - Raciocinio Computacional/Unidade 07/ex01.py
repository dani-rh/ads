import json

def escrever(data, arquivo):
    with open(arquivo+'.json', 'w') as f:
        json.dump(data,f)
        f.close()
    
def ler(arquivo):
    dados = {}
    with open(arquivo+'.json', 'r') as f:
        dados = json.load(f)
        f.close()
        return dados

dicionario=[{"Nome": "João", "Sobrenome": "Silva"},
            {"Nome": "Maria", "Sobrenome": "Ferreira"}]


escrever(dicionario, "pessoas")
dadosretornados = ler("pessoas")
print(dadosretornados)

