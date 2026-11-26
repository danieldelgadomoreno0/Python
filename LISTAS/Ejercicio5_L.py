# Escribir un programa que almacene en una lista los números del 1 al 10 y los
# muestre por pantalla en orden inverso separados por comas.
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(9,-1,-1):
    if i > 0:
        print(n[i], end=", ")
    else:
        print(n[i], end="")