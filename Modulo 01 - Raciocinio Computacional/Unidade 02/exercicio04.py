'''Crie um programa que solicite ao usuário o seu salário. Se o valor for inferior a R$ 5.000, calcule um abono de fim de ano de 15%. Caso contrário, o abono será de 10%. Informe ao usuário seu valor de abono de fim de ano.'''

salario = float(input("Digite seu salário:"))

abono = 0
if salario < 5000:
    abono = salario * 0.15
else:
    abono = salario * 0.1
print(f"Valor do seu abono de fim de ano: R${abono:.2f}")