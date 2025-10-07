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