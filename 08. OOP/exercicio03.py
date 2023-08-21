'''3. Crie uma classe Funcionario com os atributos nome e salario. Em seguida, crie um método para calcular o salário anual do funcionário, incluindo o décimo-terceiro salário. Crie um objeto dessa classe com salário definido e exiba na tela o salário anual.'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_salario_anual(self):
        return self.salario * 13
    
# Cria um objeto
funcionario1 = Funcionario("João", 3000)

#Calcula o salário anual
salario_anual = funcionario1.calcular_salario_anual()

#Exibe na tela
print("O salário anual do funcionário {} é de R$ {:.2f}".format(funcionario1.nome, salario_anual))

