def cadena_mas_larga(lista):
    mayor = 0
    mas_caracteres = 0
    cadena_mayor = ""
    desempate = ""
    for i in lista:
        if len(i) > mayor:
            mayor = len(i)
            cadena_mayor = i
            for x in i:
                if x not in desempate:
                    desempate += x
                    mas_caracteres = len(desempate)
            desempate = ""
        elif len(i) == mayor:
            for x in i:
                if x not in desempate:
                    desempate += x
                    if mas_caracteres < len(desempate):
                        mas_caracteres = len(desempate)
                        cadena_mayor = i
            desempate = ""

            
    return print(f"La cadena mas larga es {cadena_mayor} con {mayor} caracteres de los cuales {mas_caracteres} son diferentes")

cadena_mas_larga(["hola", "adios","buenos", "dias", "alvaro"])