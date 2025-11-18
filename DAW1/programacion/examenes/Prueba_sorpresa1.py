def cifrado_cesar(palabra, posicion):
    palabra = palabra.upper()
    abecedario = ["A","B","C","D","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cifrado =""
    vuelta = 0

    for i in palabra:
        if i in abecedario:
            for j in range(len(abecedario)):
                if i == abecedario[j]:
                    if len(abecedario[j+posicion]) > len(abecedario):
                        vuelta = len(abecedario[j:len(abecedario)]) - posicion
                        cifrado += abecedario[vuelta]
                    else:
                        cifrado += abecedario[j+posicion]


    return print(cifrado)

cifrado_cesar("javeir", 3)



def equivalentes_al_cifrado(palabra1, palabra2, posicion):
    palabra1 = palabra1.upper()
    palabra2 = palabra2.upper()
    abecedario = ["A","B","C","D","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    cifrado =""

    for i in palabra1:
        if i in abecedario:
            for j in range(len(abecedario)):
                if i == abecedario[j]:
                    cifrado += abecedario[j+posicion]

    return print(f"{palabra1} y {palabra2} son equivalentes y utilizan un nivel de codificacion {posicion}") if cifrado == palabra2 else print("No son equivalentes")


