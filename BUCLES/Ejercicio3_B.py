n = int(input("Dime un numero positivo: "))
num_print = ""
for i in range(1, n):
    if i % 2 != 0:
        num_print += str(i) + ", "
print(num_print)