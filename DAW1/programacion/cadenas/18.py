def contar_palabras(cadena):
    contador = 1
    for i in cadena:
        if i == " ":
            contador += 1
    return contador

assert(contar_palabras("Hola soy Alvaro Cruces Martinez, me gusta entrenar calistenia y jugar videojuegos") == 12)
assert(contar_palabras("Alvaro Cruces Martinez") == 3)
assert(contar_palabras("Alvaro Cruces") == 2)
assert(contar_palabras("hola soy alvaro cruces martinez") == 5)