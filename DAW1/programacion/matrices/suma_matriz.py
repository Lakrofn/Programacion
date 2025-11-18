matriz1 = [[5,0,0], [0,9,0],[0,0,7]]
matriz2 = [[1,2,3], [1,0,3], [1,3,2]]

fila1= []
fila2= []

acumulador = 0
cadena=""


for fila in range(1,len(matriz1)):
    for celdas in range(fila):
        acumulador += matriz1[fila][celdas] + matriz2[fila][celdas]
        cadena += " " + str(acumulador)
    print(cadena)
    cadena = ""
