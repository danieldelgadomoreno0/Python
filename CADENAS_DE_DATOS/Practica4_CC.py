num = input("Dime un número de telefono completo: ")
#sepa = num.split("-")
sepa = num[3:10]
print (f"El numero de telefono sin pprefijo y extensión es: {sepa}")
