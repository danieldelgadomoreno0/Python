n = int(input("Introduce la altura del triángulo: "))
# range(inicio, hasta que número, incremento)
# Bucle para cada fila con números impares (1, 3, 5, ...)
for i in range(1, n, 2):
    # Imprime desde i hasta 1 bajando de 2 en 2
    for j in range(i, 0, -2):
        print(j, end=" ")   
    print() # Salto de línea