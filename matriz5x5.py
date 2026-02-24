matriz = []

for i in range(5):
    fila = []
    for j in range(5):
        numero = int(input(f"Ingrese número para posición [{i}][{j}]: "))
        fila.append(numero)
    matriz.append(fila)

print("\nMatriz 5x5:")
for fila in matriz:
    print(fila)