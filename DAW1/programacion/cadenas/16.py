def contadordecaracteres(cadena):
    abecedario = ""
    contador = 0
    for i in cadena.lower():
        if i not in abecedario and i != " ":
            contador += 1
            abecedario += i
    return contador

print(contadordecaracteres("El perro de la zanahoria"))