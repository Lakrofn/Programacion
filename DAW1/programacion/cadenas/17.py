def separar_y_juntar(cadena):

    consonantes = ""
    vocales = "aeiouAEIOU"
    sonvocales = ""

    for i in cadena:
        if i != " ":
            if i in vocales:
                sonvocales += i
            else:
                consonantes += i
    
    return consonantes + sonvocales

print(separar_y_juntar("Hola soy Alvaro Cruces Martinez, me gusta entrenar calistenia y jugar videojuegos"))