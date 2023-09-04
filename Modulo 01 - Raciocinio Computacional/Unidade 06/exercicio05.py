'''Exercício de fixação 5: Documente a função media() desenvolvida no exercício de fixação 3 desta unidade.'''

def media(*numeros):
    """
    Calcula a média dos números passados para a função
   
    :param numeros: lista de números
    :return: valor da média calculada
    """
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)