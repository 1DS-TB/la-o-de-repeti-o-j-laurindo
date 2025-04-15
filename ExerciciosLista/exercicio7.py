N = int(input("Digite um número: "))
linha = 1

if N > 0:
    while linha <= N:
        icone = linha
        while icone > 0:
            print("*", end="")
            icone -= 1
        print()
        linha += 1
else:
    print("NÚMERO INVÁLIDO")