nomb = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo(mujer/hombre): ")
if nomb < "m" and sexo == "mujer" or nomb > "n" and sexo == "hombre":
    print("Tu vas al grupo A")
else:
    print("Tu vas al grupo B")
