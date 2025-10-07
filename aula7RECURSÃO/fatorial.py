def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fat = n * (n-1)
        return fatorial(n - 1)
print(fatorial(6))