

def subcuadricula(tablero):
    comprobaciones = []
    valido = True
    bloques = []
    actual = 0
    for fila in tablero:
        for columna in fila:
            for subcuadro in columna:
                for numero in subcuadro:
                    bloques.append(numero)
                    comprobaciones.append(numero)
            for comprobar in bloques:
                actual = comprobar
                comprobaciones.remove(comprobar)
                if actual in comprobaciones:
                    valido = False
            bloques = []
    return valido

def filas(tablero):
    comprobaciones = []
    bloques = []
    fila1 = []
    fila2 = []
    fila3 = []
    actual = 0
    valido = True
    for filas in range(len(tablero)):
        for columna in range(len(tablero[filas])):
            for fila_exacta in range(len(tablero[filas][columna])):
                for numero in tablero[filas][columna][fila_exacta]:
                    if fila_exacta == 0:
                        fila1.append(numero)
                    elif fila_exacta == 1:
                        fila2.append(numero)
                    else:
                        fila3.append(numero)
        bloques.append(fila1)
        fila1 = []
        bloques.append(fila2)
        fila2 = []
        bloques.append(fila3)
        fila3 = []
        for fila in bloques:
            for numero in fila:
                comprobaciones.append(numero)
            for comprobar in fila:
                actual = comprobar
                comprobaciones.remove(comprobar)
                if actual in comprobaciones:
                    valido = False
        bloques = []
    return valido

def columnas(tablero):
    columnas = []
    comprobaciones = []
    bloques = []
    columna1 = []
    columna2 = []
    columna3 = []
    actual = 0
    valido = True
    for fila in tablero:
        for columna in range(len(fila)):
            if columna == 0:
                columna1.append(fila[columna])
            elif columna == 1:
                columna2.append(fila[columna])
            else:
                columna3.append(fila[columna])
    columnas.append(columna1)
    columna1 = []
    columnas.append(columna2)
    columna2 = []
    columnas.append(columna3)
    columna3 = []
    for cuadricula in columnas:
        for fila_cuadricula in cuadricula:
            for columna_cuadricula in fila_cuadricula:
                for numero in range (len(columna_cuadricula)):
                    if numero == 0:
                        columna1.append(columna_cuadricula[numero])
                    elif numero == 1:
                        columna2.append(columna_cuadricula[numero])
                    else:
                        columna3.append(columna_cuadricula[numero])
        bloques.append(columna1)
        columna1 = []
        bloques.append(columna2)
        columna2 = []
        bloques.append(columna3)
        columna3 = []
        for columna_exacta in bloques:
            for numero in columna_exacta:
                comprobaciones.append(numero)
            for comprobar in columna_exacta:
                actual = comprobar
                comprobaciones.remove(comprobar)
                if actual in comprobaciones:
                    valido = False
        bloques = []
    return valido

def sudoku():
    valido = True
    tablero = [[[[1,2,3],[4,5,6],[7,8,9]],[[4,5,6],[7,8,9],[1,2,3]],[[7,8,9],[1,2,3],[4,5,6]]],[[[2,3,1],[5,6,4],[8,9,7]],[[5,6,4],[8,9,7],[2,3,1]],[[8,9,7],[2,3,1],[5,6,4]]],[[[3,1,2],[6,4,5],[9,7,8]],[[6,4,5],[9,7,8],[3,1,2]],[[9,7,8],[3,1,2],[6,4,5]]]]

    tabla = ""
    for i in tablero:
        for j in range (len(i)):
            for m in range(len(i[j])):
                for n in range(len(i[j][m])):
                    if m == 0:
                        tabla += " " + str(i[j][m][n]) 
                    elif m == 1:
                        tabla += " " + str(i[j][m][n])
                    elif m == 2:
                        tabla += " " + str(i[j][m][n])
            tabla += "\n"
    print (tabla)

    if filas(tablero=tablero) == False:
        valido = False
    elif columnas(tablero=tablero) == False:
        valido = False
    elif subcuadricula(tablero=tablero) == False:
        valido = False
    
    if valido == True:
        print("El sudoku es valido")
    else:
        print("El sudoku no es valido")

sudoku()