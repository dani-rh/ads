'''Escreva um código que solicite o preço de um produto e, caso o valor seja maior que R$ 100,00, aplique um desconto de 10%. Caso contrário, não aplique nenhum desconto e informe o preço final ao usuário.'''

preco = float(input("Digite o preço do produto: "))

valor = preco - (preco/100)*10

if preco > 100.00:
    input(f"O valor com desconto é de R$ {valor}")
else:
    input(f"O valor é de R${preco}")
