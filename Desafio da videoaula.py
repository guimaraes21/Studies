import math

# Recebe os coeficientes a, b e c da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica o valor do discriminante para determinar o tipo de raízes
if delta < 0:
    print("Esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"A raiz dupla desta equação é {raiz:.1f}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    if raiz1 > raiz2:
        raiz1, raiz2 = raiz2, raiz1
    print(f"As raízes da equação são {raiz1:.1f} e {raiz2:.1f}")
