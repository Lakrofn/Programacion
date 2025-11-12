def comprobarcasa():
    casos = int(input("Cuantas pruebas vas a hacer?"))
    contador = 0
    salida = ""
    while contador < casos:
        casa = input("Escribe el tipo de casas o colgantes o colgadas da igual mayusculas o minusculas: ")
        if casa.lower() == "colgantes":
            salida += "Mal" + "\n"
            contador += 1
        else:
            salida += "Bien" + "\n"
            contador += 1
    return salida[:-1]

print(comprobarcasa())
