def imprime_decrescente(N):
    if N < 0:
        return
    print(N)
    imprime_decrescente(N - 1)

n = int(input("Digite um número inteiro positivo: "))
print(f"Números de {n} até 0 em ordem decrescente:")
imprime_decrescente(n)