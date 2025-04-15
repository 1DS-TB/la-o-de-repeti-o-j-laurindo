N = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))

anterior = 0
sequencia = []
proxima = 1
soma = 1

if N >= 1:
    for n in range(0,N):
        sequencia.append(anterior)
        soma = proxima + anterior
        anterior = proxima
        proxima = soma
    print(f"Primeiros números da sequência = {sequencia}")
else:
    print("NÚMERO INVÁLIDO")