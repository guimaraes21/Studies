numeros = []
for i in range(3):
    numeros.append(int(input(f"Digite o {i+1} número: ")))
if numeros == sorted(numeros):
    print("Crescente")
else:
    print("Não está em ordem crescente")