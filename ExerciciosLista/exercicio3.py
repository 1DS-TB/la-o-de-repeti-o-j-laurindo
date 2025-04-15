num = int(input("Digite um número para ver sua tabuada (1 ao 10): "))
tabuada = 1

for n in range(1,11):
    tabuada = n * num
    if num > 0:
        print(f"{num} * {n} =", tabuada)
    else:
        print("NÚMERO INVÁLIDO")


