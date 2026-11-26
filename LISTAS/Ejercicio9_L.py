# Escribir un programa que pida al usuario una palabra y muestre por pantalla el
# número de veces que contiene cada vocal.
palabra = input("Escribe una palabra: ")
list = list(palabra)
a = 0
e = 0
i = 0
o = 0
u = 0
for lista in list:
    if lista == "a":
        a = a + 1
    if lista == "e":
        e = e + 1
    if lista == "i":
        i = i + 1
    if lista == "o":
        o = o +1
    if lista == "u":
        u = u + 1
print (f"En la palabra {palabra} hay {a}-a {e}-e {i}-i {o} o-{u}-u vocales")