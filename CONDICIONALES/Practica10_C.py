# .strip() lo que hace es eliminar los espacios en caso de que hayas puesto por error
tipo = input("¿Deseas una pizza vegetariana? (responde 'si' o 'no'): ").strip().lower()

if tipo == "si":
    print("\nIngredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
    
    opcion = input("Elige un ingrediente escribiendo 1 o 2: ").strip()
    
    if opcion == "1":
        ingrediente = "Pimiento"
    elif opcion == "2":
        ingrediente = "Tofu"
    else:
        ingrediente = "nada"

    if ingrediente:
        print("\nTu pizza es vegetariana.")
        print(f"Ingredientes: mozzarella, tomate y {ingrediente.lower()}.")
    else:
        print("\nLa opción elegida no es válida.")

elif tipo == "no":
    print("\nIngredientes no vegetarianos disponibles:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    
    opcion = input("Elige un ingrediente escribiendo 1, 2 o 3: ").strip()
    
    if opcion == "1":
        ingrediente = "Peperoni"
    elif opcion == "2":
        ingrediente = "Jamón"
    elif opcion == "3":
        ingrediente = "Salmón"
    else:
        ingrediente = "nada"

    if ingrediente:
        print("\nTu pizza no es vegetariana.")
        print(f"Ingredientes: mozzarella, tomate y {ingrediente.lower()}.")
    else:
        print("\nLa opción elegida no es válida.")

else:
    print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")