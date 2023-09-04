def maior_menor(*numeros):
    """
    Recebe uma lista aleatória de números e calcula o maior e o menor deles
    
    Args: 
        numeros: lista de números a ser analisados
    Returns: 
        Retorna o maior e o menor número da lista
    """
    maior = -100000
    menor = 100000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor