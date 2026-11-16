lote = []
for i in range(0,3):
    loteria = input("Escriba los números ganadores de la lorería: ")
    lote.append(loteria)
if lote[0] > lote[1]:
    lote[0], lote[1] = lote[1], lote[0]
if lote[0] > lote[2]:
    lote[0], lote[2] = lote[2], lote[0]
if lote[1] > lote[2]:
    lote[1], lote[2] = lote[2], lote[1]
print(lote[0], lote[1], lote[2])