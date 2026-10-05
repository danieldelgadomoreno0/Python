precio = input("Introduce el precio en euros con dos decimales (importante separado por .): ")
partes = precio.split(".")
euros = partes[0]
centimos = partes[1]
print(f"El precio contiene {euros} euros y {centimos} céntimos")