N = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))
a = 0
b = 1

for i in range(N):
    print(a, end=" ")
    a, b = b, a + b