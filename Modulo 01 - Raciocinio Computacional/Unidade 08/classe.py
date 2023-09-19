# # Classe Cliente

# class Cliente:
 
#     def __init__(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf
 
#     def alterar_dados(self, nome, cpf):
#         self.nome = nome
#         self.cpf = cpf
 
#     def imprimir(self):
#         print(f"Cliente:", self.nome, "- CPF:", self.cpf)
 
 
# cliente = Cliente("João", "123.456.789-00")
# cliente.imprimir()

# Exemplo com escopo privado
class Cliente:
 
    def __init__(self, nome, cpf):
        self.__nome = nome
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = "CPF inválido"
 
    def imprimir(self):
        print(f"Cliente:", self.__nome, "- CPF:", self.__cpf)
 
    def mudar_cpf(self, cpf):
        if self.__cpf_valido(cpf):
            self.__cpf = cpf
        else:
            self.__cpf = "CPF inválido"
 
    def ler_cpf(self):
        return self.__cpf
 
    def __cpf_valido(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False
 
 
cliente = Cliente("João", "12345678900")
print(cliente.ler_cpf())
cliente.mudar_cpf("12345")
print(cliente.ler_cpf())