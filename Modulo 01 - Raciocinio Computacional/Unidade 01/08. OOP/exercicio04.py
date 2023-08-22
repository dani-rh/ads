'''4. Crie uma classe Estudante com os atributos nome, idade e nota. Em seguida, crie um método para calcular a média das notas de dois alunos. Crie dois objetos dessa classe com notas definidas e exiba na tela a média calculada.'''

class Estudante:
    def __init__ (self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        
    def calcular_media(self, outro_estudante):
        media = (self.nota + outro_estudante.nota) / 2
        return media
    
#Cria dois objetos
estudante1 = Estudante("Ana", 20, 8.5)
estudante2 = Estudante("João", 19, 7.5)

#Chama o método
media_notas = estudante1.calcular_media(estudante2)

#Exibe a média
print("A média das notas dos estudantes {} e {} é: {}".format(estudante1.nome, estudante2.nome, media_notas))