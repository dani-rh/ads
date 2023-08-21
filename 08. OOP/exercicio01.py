'''Crie uma classe chamada Animal com atributos nome e especie. Crie um método para mostrar na tela o som que o animal faz. Crie um objeto para demonstrar o seu uso.'''

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        
    def fazer_som(self):
        print("{} está fazendo um som de {}".format(self.nome, self.especie))
        
# Cria um objeto da classe animal
meu_animal = Animal("Kora", "cachorro")

# Chama o método som do objeto criado
meu_animal.fazer_som()