def Multip_Rec(n1, n2):
    # Caso base
    if n2 == 0:
        return 0

    elif n2 < 0:
        return -Multip_Rec(n1, -n2)
    else:
        return n1 + Multip_Rec(n1, n2 - 1)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"{a} x {b} = {Multip_Rec(a, b)}")