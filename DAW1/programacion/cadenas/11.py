def sacar_numeros_armstrong():
    acumulador = ""
    contador = 0
    suma = 0
    for i in range(1, 999 + 1):
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

print(sacar_numeros_armstrong())