num = int(input("Insira um número inteiro positivo e calcule seu fatorial: "))
numeros = []
resultado = 1

if num > 0:
    for n in range(1, num+1):
        resultado *= n
        numeros.append(n)
    print(f"{num}! = {numeros} = {resultado}")
elif num == 0:
    print(f"{num}! = ", 1)
else:
    print("VALOR INVÁLIDO")