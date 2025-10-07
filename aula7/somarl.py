def somar_l(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somar_l(lista[1:])
numerosx = [1,3,5,7,11]
print(somar_l(numerosx))