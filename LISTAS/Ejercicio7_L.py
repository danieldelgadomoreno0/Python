# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
# resultante.
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
n = []
for i in range(2, len(abecedario), +3):
    n.append(abecedario[i])
for letra in n:
    abecedario.remove(letra)
# del abecedario[2::3] #esta es otra forma de hacerlo
print(abecedario)