def reversa(lista):
    lista_reversa = []
    for i in range(-1, -len(lista)-1, -1):
        lista_reversa.append(lista[i])
    return lista_reversa

print(reversa(["di", "buen", "dia", "a", "papa"]))