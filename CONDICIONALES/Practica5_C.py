edad = int(input("Que edad tienes: "))
ingreso = float(input("Cuanto ingresas mensualmente: "))
if (edad > 16 and ingreso >= 1000.00):
    print("Tienes que tributar")
else:
    print("No tienes que tributar")