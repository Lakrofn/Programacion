def suma_numeros_en_cadena(cadena):
    numeros = "0123456789"

    acumulador = ""
    suma = 0

    for i in cadena:
        if i in numeros:
            acumulador += i
        else:
            if acumulador != "":
                suma += int(acumulador)
                acumulador = ""
    if acumulador != "":
        suma += int(acumulador)
        acumulador = ""

    return suma


assert(suma_numeros_en_cadena("abc12x3y45") == 60)
assert(suma_numeros_en_cadena("abc123x45") == 168)
assert(suma_numeros_en_cadena("1a2b3c4d5e6f7g8h9") == 45)