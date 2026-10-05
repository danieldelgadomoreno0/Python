correo = input("Cual es tu correo: ")
correo_sepa = correo.split("@")
correo_final = correo_sepa[0] + "@ceu.es"
print (f"Tu nuevo correo es {correo_final}")