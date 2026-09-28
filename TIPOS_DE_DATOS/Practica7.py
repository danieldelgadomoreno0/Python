peso = float(input("¿Cual es tu peso? "))
altura = float(input("¿Cual es tu estatura? "))
imc = round(peso / (altura**2),2)
print (f"Tu indice de masa corporal es de {imc}")