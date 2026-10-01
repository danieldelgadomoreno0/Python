i = float(input("Inserta la cantidad a invertir "))
ia = float(input("Inserta el interes anual "))
a = int(input("Inserta la cantidad de años "))
interessimple = round(i * (ia / 100) * a)
capital_total = i + interessimple
print(f"Teniendo en cuenta los datos que has dado tu interes generado sera de {interessimple}€")
print(f"Y el capital total sera {capital_total}€")