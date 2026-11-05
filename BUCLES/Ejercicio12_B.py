frase = input("Escribe una frase: ")
letra = input("Escribe una letra: ")
cont = 0
for i in frase:
    if letra == i:
        cont = cont + 1
print(f"{cont}")