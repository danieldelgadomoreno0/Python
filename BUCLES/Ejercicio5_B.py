can = float(input("Cual es tu cantidad a invertir: "))
interes = float(input("Cual es el interes: "))
anios = int(input("Para cuantos años: "))
cap_obtenido = 0
cap_final = 0
for i in range(1,anios+1):
    cap_obtenido = can*(interes/100)*i
    cap_final = can + cap_obtenido
    print(f"El capital obtenido en el año {i} es de {cap_obtenido} y la capital total es de {cap_final}")