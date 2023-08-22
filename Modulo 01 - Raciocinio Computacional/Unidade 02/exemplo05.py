# print("Por favor, insira tres números diferentes:")
# num1 = float(input("Digite o primeiro número:"))
# num2 = float(input("Digite o segunda número:"))
# num3 = float(input("Digite o terceiro número:"))

# # Verifica se os números sao diferentes
# if num1 == num2:
#     print("Os números inseridos nao sao diferentes.")
# else:
#     if num1 == num3:
#         print("Os números inseridos nao sao diferentes.")
#     else:
#         if num2 == num3:
#             print("Os números inseridos nao sao diferentes.")  
#         else:
#             menor = num1
            
#             if num2 < menor:
#                 menor = num2
#             if num3 < menor:
#                 menor = num3
            
#             print(f"O menor número é: {menor}")
            
            
# Exemplo 05 usando o elif
print("Por favor, insira tres números diferentes:")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segunda número:"))
num3 = float(input("Digite o terceiro número:"))

# Verifica se os números sao diferentes
if num1 == num2:
    print("Os números inseridos nao sao diferentes.")
elif num1 == num3:
    print("Os números inseridos nao sao diferentes.")
elif num2 == num3:
    print("Os números inseridos nao sao diferentes.")  
else:
    if num1 < num2:
        if num1 < num3:
            print("O menor número é:", num1)       
        else:
            print("O menor número é:", num2)
    elif num2 < num3:
        print("O menor número é:", num2)
    else:
        print("O menor número é:", num3)
        