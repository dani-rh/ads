'''5. Crie uma classe chamada Livro com atributos titulo, autor e ano_publicacao. Crie um método para imprimir as informações do livro. Crie um objeto para demonstrar o seu uso.'''

class Livro:
    def __init__(self, titulo_informado, autor_informado, ano_publicacao_informado):
        self.titulo = titulo_informado
        self.autor = autor_informado
        self.ano_publicacao = ano_publicacao_informado
    
    def mostrar_informacoes(self):
        print("Título: {}".format(self.titulo))
        print("Autor: {}".format(self.autor))
        print("Ano de publicação: {}".format(self.ano_publicacao))

# Cria um objeto da classe Livro
meu_livro = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J. R. R. Tolkien", 1954)

# Chama o método imprimir_info do objeto criado
meu_livro.mostrar_informacoes()