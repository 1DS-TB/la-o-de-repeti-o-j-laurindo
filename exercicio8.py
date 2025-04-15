num = int(input("Digite o valor que deseja calcular a série harmônica: "))
soma = 0
contador = 1

if num > 0:
    while contador <= num:
        valor = 1 / contador
        soma += valor
        contador += 1
    print(f"A soma final da série harmônica com {num} é: {soma:.2f}")
else:
    print("NÚMERO INVÁLIDO")
