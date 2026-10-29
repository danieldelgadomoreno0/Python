passwd = "contraseña"
x = 0
while x == 0:
    passwd_w = input("Escribe la contraseña: ")
    if passwd_w == passwd:
        print("Contraseña correcta!!")
        x += 1
    else:
        print("Contraseña incorrecta intentelo de nuevo")