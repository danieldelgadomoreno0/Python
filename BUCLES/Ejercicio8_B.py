n = int(input("Introduce la altura del triángulo: "))
# range(inicio, hasta que número, incremento)
for i in range(1, n, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")   
    print()