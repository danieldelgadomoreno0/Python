# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
# palíndromo.
palabras = ["oso", "rapar", "pata","ama"]
for i in palabras:
    if i[::-1] == i:
        print(f"La palabra es palíndromo: {i}")
    else:
        print(f"La palabra {i} no es palíndromo")