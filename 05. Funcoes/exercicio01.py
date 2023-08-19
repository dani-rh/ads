'''Crie uma função que recebe três notas. Ela deve retornar a média dessas notas para o usuário.'''

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(8.5, 9.0, 7.1)
print(resultado)