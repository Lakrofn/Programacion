def contar(cadena, buscar):
    contador = 0
    posicion = 0
    for i in cadena:
        if len(buscar) != posicion:
            if i == buscar[posicion]:
                posicion += 1
            else:
                posicion = 0
        else:
            contador += 1
            posicion = 0
    if len(buscar) == posicion:
        contador += 1
    return contador

assert (contar("ATCGTTCTCGTTGATCTCGTTATCTCG", "CGTT") == 3)
assert (contar("ATCGTTCTCGTTGATCTCGTTATCTCG", "CGAA") == 0)
assert (contar("ATCGTTCTCGTTGATCTCGTTATCTCG", "CG") == 4)

def descomprimir(cadena):
    numeros = ""
    letras = ""
    acumulador = ""

    for i in cadena:
        if i.isdigit():
            numeros += i
        else:
            letras += i
    
    for numero in range (len(numeros)):
        for letra in range (len(letras)):
            if numero == letra:
                acumulador += letras[letra] * int(numeros[numero])
                
    return acumulador

assert (descomprimir("A3G2T1C3") == "AAAGGTCCC")
assert (descomprimir("A1G1T1C3") == "AGTCCC")
assert (descomprimir("A2L1R2O3") == "AALRROOO")

def descomprimir2(cadena):
    acumulador = []
    numeros = []
    letras = []
    resultado = ""
    for i in cadena:
        if i.isdigit():
            numeros.append(i)
        else:
            if numeros != []:
                acumulador.append(numeros)
                numeros = []
            letras.append(i)
    acumulador.append(numeros)
    numeros = []
    for i in acumulador :
        if len(i) > 1:
            numeros.append(i[0] + i[1])
        else:
            numeros.append(i[0])
    for i in range(len(numeros)):
        for j in range(len(letras)):
            if i == j:
                resultado += letras[j] * int(numeros[i])
    return resultado

assert (descomprimir2("A10G11T1C3") == "AAAAAAAAAAGGGGGGGGGGGTCCC")
assert (descomprimir2("A1G1T1C20") == "AGTCCCCCCCCCCCCCCCCCCCC")

def comprimir(cadena):
    acumulador = ""
    letras = ""
    contador = 0
    
    for i in cadena:
        if i not in letras:
            letras += i
    for i in letras:
        acumulador += i
        for j in cadena:
            if i == j:
                contador += 1
            else:
                if contador > 0:
                    acumulador += str(contador)
                    contador = 0
    acumulador += str(contador)

    
    return acumulador

assert (comprimir("AAAGGTCCC") == "A3G2T1C3")
assert (comprimir("AGTCCC") == "A1G1T1C3")
assert (comprimir("AALRROOO") == "A2L1R2O3")