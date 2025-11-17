def ordenar_por_palabras(lista, palabra):
    lista_ordenada = []
    for i in lista:
        if i[0].lower() == palabra.lower():
            lista_ordenada.append(i)
    return lista_ordenada

print(ordenar_por_palabras(["alvaro", "adrian", "joel", "javier", "alejandro"], "a"))