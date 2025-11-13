def siglas(cadena):
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    palabra = ""
    acumulador = ""

    for letra in cadena:
        palabra += letra
        if letra == " ":
            if palabra[0] in abecedario:
                acumulador += palabra[0]
                palabra = ""
            else:
                palabra = ""
    if palabra[0] in abecedario:
        acumulador += palabra[0]

    return acumulador

assert(siglas("Asociación de Técnicos en Informática") == "ATI")
assert(siglas("Asociación de Técnicos en Informática y Tecnología") == "ATIT")
assert(siglas("asociación de Técnicos en Informática") == "TI")
assert(siglas("asociación de técnicos en informática") == "")