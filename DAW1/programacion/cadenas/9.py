def palabra_escondida(cadena, palabra):
    reduccion = palabra.lower()
    resultado = ""
    for i in cadena:
        while len(reduccion) > 0 and reduccion[0] in i:
            resultado += i
            reduccion = reduccion[1:]
        
    if resultado == palabra:
        return True
    else:
        return False
    
assert(palabra_escondida("supercalifragilisticoespialidoso","rapido")== True)
assert(palabra_escondida("supercalifragilisticoespialidoso","oso")== True)
assert(palabra_escondida("supercalifragilisticoespialidoso","superespia")== True)
assert(palabra_escondida("supercalifragilisticoespialidoso","fragiles")== True)