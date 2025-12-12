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