def cadena_mas_larga(lista):
    mayor = 0
    cadena_mayor = ""
    for i in lista:
        if len(i) > mayor:
            mayor = len(i)
            cadena_mayor = i
        elif len(i) == mayor:
            cadena_mayor +=" " + "y" + " " + i
    return print(f"La cadena mas larga es/son {cadena_mayor} con {mayor} caracteres")

cadena_mas_larga(["hola", "adios", "buenos", "dias", "alvaro"])