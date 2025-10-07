def somar_l(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somar_l(lista[1:])
numerosx = [1,3,5,7,11]
print(somar_l(numerosx))


def max_l(lista):
    if len(lista) == 0:
        print("LISTA VAZIA")
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        max_rest = max_l(lista[1:])
        if lista[0] > max_rest:
            return lista[0]
        else:
            return max_rest
numerosy = [1,3,5,7,11]
print(max_l(numerosy))


def min_l(lista):
    if len(lista) == 0:
        print("LISTA VAZIA")
        return None
    elif len(lista) == 1:
        return lista[0]
    else:
        min_rest = min_l(lista[1:])
        if lista[0] < min_rest:
            return lista[0]
        else:
            return min_rest
numerosz = [1,3,5,7,11]
print(min_l(numerosz))


def media_r(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        soma_restante = media_r(lista[1:]) * (len(lista) - 1)
        return (lista[0] + soma_restante) / len(lista)

numeroxx = [4,5,6,7,8]
print(media_r(numeroxx))


def somatorio(n):
    if n == 1:  
        return 1
    else:
        return n + somatorio(n - 1)  
num = int(input("Digite um número inteiro positivo: "))
print("O somatório de 1 até", num, "é:", somatorio(num))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Digite um número inteiro positivo: "))
print(f"O Fibonacci de {num} é {fibonacci(num)}")


def fatorial(n):
    if n2 == 0 or n2 == 1:
        return 1
    else:
        fat = n2 * (n2-1)
        return fatorial(n2 - 1)
print(fatorial(6))

def mult_rec(n1,n2):
