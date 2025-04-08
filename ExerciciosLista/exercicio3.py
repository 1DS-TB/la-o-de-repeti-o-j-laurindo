num = int(input("Digite um número para ver sua tabuada (1 ao 10): "))
tabuada = 1

## INSERIR VALIDAÇÃO
for n in range(1,11):
    tabuada = n * num
    print(f"{num} * {n} =", tabuada)

