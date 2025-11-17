def lista_ordenada(lista):
    numero_anterior = lista[0]
    boleano = True
    for i in lista:
        if i != 0 and i - 1 == numero_anterior:
            numero_anterior = i
        else:
            boleano = False
        
    return boleano

assert lista_ordenada([1,2,3,4,5])
assert not lista_ordenada([1,3,4,5])

            
