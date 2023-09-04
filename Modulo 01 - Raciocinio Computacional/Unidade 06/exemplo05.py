def delta(a, b, c):
    return b*b - 4*a*c
 
def bhaskara(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("As raízes são imaginárias")
        return 0, 0, False
    else:
        x1 = (-b + d ** 0.5) / 2 * a
        x2 = (-b - d ** 0.5) / 2 * a
        return x1, x2, True
 
result1 = bhaskara(1, 3, 1)
if result1[2]:
    print(f"As raízes são {result1[0]} e {result1[1]}")
 
result2 = bhaskara(1, 2, 1)
if result2[2]:
    print(f"As raízes são {result2[0]} e {result2[1]}")
 
result3 = bhaskara(1, 1, 1)
if result3[2]:
    print(f"As raízes são {result3[0]} e {result3[1]}")