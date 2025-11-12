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
    
print(palabra_escondida("supercalifragilisticoespialidoso","rapido"))