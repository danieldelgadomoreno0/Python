renta = float(input("Cual es tu renta anual: "))
if renta < 10000:
    print("5%")
if renta >= 10000 and renta < 20000:
    print("15%")
if renta >= 20000 and renta < 35000:
    print("20%")
if renta >= 35000 and renta < 60000:
    print("30%")
if renta >= 60000:
    print("45%")