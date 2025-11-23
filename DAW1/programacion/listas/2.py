def desplazamiento(desplazar,direccion):
    lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    if direccion == "D":
        contador = 0
        while contador < desplazar:
            lista.insert(0, lista.pop(-1))
            contador += 1
    elif direccion == "I":
        contador = 0
        while contador < desplazar:
            lista.append(lista.pop(0))
            contador += 1
    else:
        print("La direccion no es valida")
    return lista
print(desplazamiento(5,"D"))
print(desplazamiento(5,"I"))