N = int(input("Digite um número: "))
linha = 1

if N > 0:
    while linha <= N:
        i = linha
        while i > 0:
            print("*", end="")
            i -= 1
        print()
        linha += 1
else:
    print("NÚMERO INVÁLIDO")