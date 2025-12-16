def fila(tablero):
    sumafinal = 0
    acumulador = []
    valido = True
    for fila in tablero:
        suma = 0
        for columna in fila:
            if fila == tablero[0]:
                sumafinal += columna
                suma += columna
            else:
                suma += columna
        acumulador.append(suma)
    for numero in acumulador:
        if numero != sumafinal:
            valido = False
    return valido


def diagonal(tablero):
    direccion = 0
    sumafinal=15
    contador = 0
    comprobaciones = 0
    acumulador = []
    valido = True
    while comprobaciones < 2:
        suma = 0
        if direccion == 0:
            for fila in tablero:
                suma += fila[contador]
                contador +=1
            comprobaciones += 1
            direccion += 1
            acumulador.append(suma)
        else:
            contador = len(tablero[0]) - 1
            for fila in tablero:
                suma += fila[contador]
                contador -= 1
            comprobaciones += 1
            acumulador.append(suma)
    for numero in acumulador:
        if numero != sumafinal:
            valido = False
    return valido


def columnas(tablero):
    columna1 = []
    columna2 = []
    columna3 = []
    sumafinal= 15
    acumulador = []
    suma = 0
    valido = True
    for columna in tablero:
        for fila in range(len(columna)):
            if fila == 0:
                columna1.append(columna[fila])
            elif fila == 1:
                columna2.append(columna[fila])
            else:
                columna3.append(columna[fila])
    acumulador.append((columna1))
    acumulador.append((columna2))
    acumulador.append((columna3))
    for columna in acumulador:
        for numero in columna:
            suma += numero
        if suma != sumafinal:
            valido = False
        suma = 0
    return valido

def es_cuadrado_magico():
    tablero = [[8,1,6],[3,5,7],[4,9,2]]
    valido = True

    if fila(tablero) == False:
        valido = False
    elif diagonal(tablero) == False:
        valido = False
    elif columnas(tablero) == False:
        valido = False

    return print(valido)

es_cuadrado_magico()
















def is_happy(numero):
    resultado = 0
    acumulador = 0
    contador = 0
    valido = False
    while resultado != 1 and resultado != numero and contador <= 8:
        if resultado == 0:
            for i in str(numero):
                resultado += int(i)**2
        else:
            for i in str(resultado):
                acumulador += int(i)**2
            resultado = acumulador
        acumulador = 0
        contador +=1
    if resultado == 1:
        valido = True
    
    return valido

assert(is_happy(17) == False)
assert(is_happy(7) == True)
assert(is_happy(13) == True)
assert(is_happy(34) == False)
assert(is_happy(19) == True)