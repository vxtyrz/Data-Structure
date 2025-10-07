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
