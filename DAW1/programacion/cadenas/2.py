def camelcase(cadena):
    palabra = ""
    palabrafinal = ""

    acumulador = ""
    for espacio in cadena:
        if espacio != " ":
            palabra += espacio
    
        else:
            for i in range(len(palabra)):
                if i == 0:
                    palabrafinal += palabra[0].upper()
                else:
                    palabrafinal += palabra[i]
            acumulador += palabrafinal
            palabra = ""
            palabrafinal = ""

    for i in range(len(palabra)):
        if i == 0:
            palabrafinal += palabra[0].upper()
        else:
            palabrafinal += palabra[i]
    acumulador += palabrafinal

    return acumulador

assert(camelcase("hola mundo como estas") == "HolaMundoComoEstas")
assert(camelcase("python es genial") == "PythonEsGenial")
assert(camelcase("hola soy alvaro cruces martinez") == "HolaSoyAlvaroCrucesMartinez")
assert(camelcase("estaesunaprueba") == "Estaesunaprueba")