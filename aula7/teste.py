def media_r(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        soma_restante = media_r(lista[1:]) * (len(lista) - 1)
        return (lista[0] + soma_restante) / len(lista)

numeroxx = [4,5,6,7,8]
print(media_r(numeroxx))