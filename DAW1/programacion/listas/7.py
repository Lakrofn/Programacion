def union_listas(lista1, lista2):
    lista_union = []
    for i in lista1:
        if i not in lista_union:
            lista_union.append(i)
    for i in lista2:
        if i not in lista_union:
            lista_union.append(i)
    return lista_union

print(union_listas([1,2,3,4,5], [2,3,4,5,6]))
    