def palindromo(cadena):
    acumulador = ""
    for i in cadena:
        if i != " ":
            acumulador += i.lower()

    if acumulador == acumulador.lower()[::-1]:
        return True
    else:
        return False

print(palindromo("se es o no se es"))