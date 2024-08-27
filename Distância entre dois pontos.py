import math
number = []
for i in range (4):
   num = int(input(f"Digite o {i+1} número: "))
   number.append(num)

equacao = math.sqrt((number[0] - number[2])**2 + (number[1] - number[3])**2)
if (equacao) >= 10:
    print("Longe")
else:
    print("perto")