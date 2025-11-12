cadena = "abc12x3y45"
numeros = "0123456789"

acumulador = ""
suma = 0

for i in cadena:
    if i in numeros:
        acumulador += i
    else:
        if acumulador != "":
            suma += int(acumulador)
            acumulador = ""
if acumulador != "":
    suma += int(acumulador)
    acumulador = ""

print(suma)