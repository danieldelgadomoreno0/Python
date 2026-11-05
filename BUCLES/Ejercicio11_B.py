palabra = input("Escribe una palabra: ")
palabra_in = ""
for caracter in palabra:
    palabra_in = caracter + " " + palabra_in
print(f"{palabra_in}")