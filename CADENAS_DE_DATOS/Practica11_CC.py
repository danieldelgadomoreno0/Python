producto = input("Digame un producto ")
precio = float(input("Digame el precio de ese producto "))
unidades = int(input("Digame la cantidad de unidades que se va a llevar "))
precio_total = precio * unidades
resultado = "{}: {:09.2f}€ x {:03d} unidades = {:011.2f}€".format(producto, precio, unidades, precio_total)
print(f"{resultado}")
#Este es otro de los metodos que he visto para hacerlo la diferencia
#es que en vez de usar el .format pone los fomatos al lado de cada variable
# print(f"{producto}: {precio:09.2f}€ x {unidades:03d} unidades = {precio_total:011.2f}€")