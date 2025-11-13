def palindromo(cadena):
    acumulador = ""
    for i in cadena:
        if i != " ":
            acumulador += i.lower()

    if acumulador == acumulador.lower()[::-1]:
        return True
    else:
        return False

assert(palindromo("se es o no se es")== True)
assert(palindromo("hola soy alvaro cruces martinez") == False)
assert(palindromo("reconocer") == True)
assert(palindromo("Se verlas al reves") == True)