n = int(input("Dame un numero entero: "))
divisor = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisor += 1
if divisor <= 2:
    print(f"El número entero {n} es primo.")
else:
    print(f"El número entero {n} no es primo.")