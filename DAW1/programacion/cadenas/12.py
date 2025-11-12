def sacar_numeros_armstrong_en_rando(rango1, rango2):
    acumulador = ""
    contador = 0
    suma = 0
    for i in range(rango1, rango2 + 1):
        for j in str(i):
            contador += 1
        for m in str(i):
            suma += int(m) ** contador
        if suma == i:
            acumulador += str(i) + ", "
            suma = 0
            contador = 0
        else:
            suma = 0
            contador = 0
    return acumulador

print(sacar_numeros_armstrong_en_rando(200, 10000))