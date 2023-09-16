'''Exemplo de aplicação 10: Mostre um menu simples com opções numéricas ao usuário. Converta a opção digitada para um número inteiro. Mostre uma mensagem simples de erro se o valor digitado for inválido (como um texto).'''

while True:
    print("1. Doces")
    print("2. Salgados")
    print("3. Bebidas")
    print("4. Sair")
    
    try:
        opcao = int(input("Digite uma opção: "))
    except:
        print("Voce digitou uma opção inválida. Tente novamente.")
        continue
    
    if opcao >=1 and opcao <= 3:
        print(f"Voce digitou a opção válida \"{opcao}\".")
    elif opcao == 4:
        break
    else:
        print("Voce digitou uma opção inválida. Tente novamente.")