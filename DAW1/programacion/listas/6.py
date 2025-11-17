def intersectar(lista1, lista2):
    lista_comun = []
    for i in lista1:
        if i in lista2 and i not in lista_comun:
            lista_comun.append(i)
    return lista_comun

print(intersectar([1,2,3,4,4,5], [2,3,4,5,6]))
            