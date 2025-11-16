def desplazamiento(posicion):
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    lista= str(lista[-posicion]) + str(lista[:-posicion])
    return lista

print(desplazamiento(1))