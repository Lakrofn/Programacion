def fila():
    tablero = [[8,1,6],[3,5,7],[4,9,2]]
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
    return print(valido)

fila()

def diagonal():
    tablero = [[8,1,6],[3,5,7],[4,9,2]]
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
    return print(valido)
diagonal()

def columnas():
    tablero = [[8,1,6],[3,5,7],[4,9,2]]
    contador = 0
    sumafinal= 15
    acumulador = []
    suma = 0
    valido = True
    for columna in range(len(tablero)):
        for fila in tablero[columna]:
            if columna == 0:
                suma += fila[contador]
                contador += 1
            elif columna == 1:
                suma += fila[contador]
                contador += 1
            else:
                suma += fila[contador]
                contador += 1
    acumulador.append(suma)
    contador = 0
    for numero in acumulador:
        if numero != sumafinal:
            valido = False

    return print(valido)

def es_cuadrado_magico():
    tablero = [[8,1,6],[3,5,7],[4,9,2]]
    acumulador = []
    suma = 0
    valido = True
    print(acumulador)

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