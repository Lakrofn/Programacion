def contadordecaracteres(cadena):
    abecedario = ""
    contador = 0
    for i in cadena.lower():
        if i not in abecedario and i != " ":
            contador += 1
            abecedario += i
    return contador

assert(contadordecaracteres("El perro de la zanahoria") == 11)
assert(contadordecaracteres("Alvaro") == 5)
assert(contadordecaracteres("Alvaro Cruces") == 9)
assert(contadordecaracteres("Hola soy Alvaro Cruces") == 11)