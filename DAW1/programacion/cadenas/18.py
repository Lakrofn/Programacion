def contar_palabras(cadena):
    contador = 1
    for i in cadena:
        if i == " ":
            contador += 1
    return contador

print(contar_palabras("Hola soy Alvaro Cruces Martinez, me gusta entrenar calistenia y jugar videojuegos"))