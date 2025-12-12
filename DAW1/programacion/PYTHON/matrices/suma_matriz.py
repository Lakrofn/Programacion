def suma_matriz(matriz1, matriz2):
    resultado = []
    acumulador = []
    for fila in range(0,len(matriz1)):
        for celdas in range(0,len(matriz1[fila])):
            acumulador.append(matriz1[fila][celdas] + matriz2[fila][celdas])
        resultado.append(acumulador)
        acumulador = []
    return resultado

print(f"La suma de las matrices es {suma_matriz([[5,0,0], [0,9,0],[0,0,7]], [[1,2,3], [1,0,3], [1,3,2]])}")


def cuadrado_matriz(matriz):
    resultado = ""
    cadena = ""
    for fila in matriz:
        for celdas in fila:
            cadena += str(celdas) + " "
        resultado += cadena + "\n"
        cadena = ""
    return resultado

print(cuadrado_matriz([[6, 2, 3], [1, 9, 3],[1, 2, 9]]))

