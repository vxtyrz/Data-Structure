def imprime_pares(N):
    if N == 0:
        print(0)
    else:
        imprime_pares(N - 2)
        print(N)


n = int(input("Digite um número inteiro positivo par: "))
if n % 2 == 0:
    print(f"Números pares de 0 até {n}:")
    imprime_pares(n)
else:
    print("Por favor, digite um número par!")