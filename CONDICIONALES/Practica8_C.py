level = float(input("Cual es tu nivel: "))
if level == 0.0:
    bono = 2400 * level
    print(f"Inaceptable ganas {bono}")
if level == 0.4:
    bono = 2400 * level
    print(f"Aceptable ganas {bono}")
if level == 0.6:
    bono = 2400 * level
    print(f"Meritorio ganas {bono}")
if level >= 0.7:
    bono = 2400 * level
    print(f"Meritorio ganas {bono}")
if level != 0.0 and level != 0.4 and level < 0.6:
    print("Este valor no es correcto")