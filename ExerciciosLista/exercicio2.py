N = int(input("Digite um número inteiro positivo: "))
contador = 0
soma = 0

## CORRIGIR
if N > 0:
    while contador <= N:
        soma += contador
        contador += 1
    print(f"A soma de todos os números de 1 até {N} é: {soma}")
else:
    print("NÚMERO INVÁLIDO")