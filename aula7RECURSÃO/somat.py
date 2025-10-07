def somatorio(n):
    if n == 1:  
        return 1
    else:
        return n + somatorio(n - 1)  
num = int(input("Digite um número inteiro positivo: "))
print("O somatório de 1 até", num, "é:", somatorio(num))