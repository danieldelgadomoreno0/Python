canti = float(input("Inserta la cantidad a invertir "))
i = 0.04
a1 = round(canti * (1 + i),2)
a2 = round(a1 * (1 + i),2)
a3 = round(a2 * (1 + i),2)
print(f"La ganacia del primer año sera de {a1}€")
print(f"La ganacia del segundo año sera de {a2}€")
print(f"La ganacia del tercer año sera de {a3}€")