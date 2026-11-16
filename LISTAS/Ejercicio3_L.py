asignaturas = ['Matemáticas', 'Física', 'Química', 'Historia' , 'Lengua']
notas = []
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas.append(nota) # añade el dato al final de la lista
print("Resumen de notas")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")