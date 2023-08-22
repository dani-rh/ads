'''Crie uma classe Calculadora com os métodos somar, subtrair, multiplicar e dividir. Crie um objeto dessa classe e utilize os métodos para realizar operações aritméticas simples.'''

class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar (self, a, b):
        return a * b
    
    def dividir (self, a, b):
        if b == 0:
            return "Não é possível dividir por zero"
        else:
            return a / b
        
# Cria um objeto da classe Calculadora
minha_calculadora = Calculadora()

# Realiza algumas operacoes
print(minha_calculadora.somar(2, 3))
print(minha_calculadora.subtrair(5, 2))
print(minha_calculadora.multiplicar(4, 6))
print(minha_calculadora.dividir(10, 5)) 
print(minha_calculadora.dividir(10, 0)) 