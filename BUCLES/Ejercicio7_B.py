mul1 = 1
mul2 = 1
result = 0
if mul1 <= 10:
    while mul1 <= 10:
        result = mul1 * mul2
        print(f"{mul1} x {mul2} = {result}")
        if mul2 <= 10:
            mul2 += 1
        if mul2 > 10:
            mul2 -= 10
            mul1 +=1
            print ("\n")

# for mul1 in range(1,11):
#     for mul2 in range(1,11):
#         print(f"{mul1} x {mul2} = {result}")
#     print("\n")