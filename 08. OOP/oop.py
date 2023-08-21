# Criando uma classe
# Construtor
class Pessoa:
    def __init__(self, nome_informado, idade_informada): 
        self.nome = nome_informado
        self.idade = idade_informada

# Objetos      
pessoa1 = Pessoa("Maria", 25)
pessoa2 = Pessoa("João", 30)
pessoa3 = Pessoa("Pedro", 20)

print(pessoa1.nome)
print(pessoa3.idade)



