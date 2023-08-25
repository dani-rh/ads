# Função enumerate

# frutas = ["Laranja", "maça", "banana", "morango", "manga", "abacaxi"]
# for i, item in enumerate (frutas):
#     if i < 3:
# 	    print(i, item)
     
frutas = ["Laranja", "maça", "banana", "morango", "manga", "abacaxi"]
pares = []
impares = []

for i, item in enumerate (frutas):
    if i % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
        
print("frutas")
for i, item in enumerate(frutas):
    print(i, item)
    
print("pares")
for item in pares:
    print(item)
    
print("impares")
for item in impares:
    print(item)

     