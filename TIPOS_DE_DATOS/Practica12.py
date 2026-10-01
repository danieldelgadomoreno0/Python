pan_no_vendido = int(input("Cuantas barras de ban no se han vendido? "))
precio_p = 3.49
desc = 0.60
barra_dec = round(precio_p * desc, 2)
precio_desc = round(precio_p - barra_dec, 2)
total_barras = round(pan_no_vendido * precio_desc, 2)
print(f"precio habitual de la barra {precio_p}€")
print(f"Descuento que se le hara {barra_dec}€")
print(f"La barras de pan ahora tienen un valor total de {total_barras}€")
