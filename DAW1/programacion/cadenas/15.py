def contar_vocales(cadena):
    palabra = ""
    vocales = "aeiouAEIOU"
    acumulador = 0
    for i in cadena:
        if i in vocales:
            if i not in palabra:
                palabra += i.lower()
                acumulador += 1
    return acumulador

assert(contar_vocales("Alvaro") == 2)
assert(contar_vocales("Enrique") == 3)
assert(contar_vocales("Isabel") == 3)