# Ejercicio 5

n = 4

print(n%2 == 0 and n>0)

# Ejercicio 6

altura = 180
ancho = 120

print(altura >= 0 and ancho >= 0)

# Ejercicio 7

nota = 8

print(nota >= 0 and nota <= 10)

# Ejercicio 8

x = 50
y = 20
z = 30

print(x + y + z == 100 and 100 - x - y - z == 0)

# Ejercicio 9

hora = 12

print(hora >= 0 and hora <= 23)

# Ejercicio 10

minuto = 30

print(minuto <= 60 and minuto >= 0)

# Ejercicio 11

colorsemaforo = "U"

print(colorsemaforo != "R" and colorsemaforo != "A" and colorsemaforo != "V")

#condicionales

# Ejercicio 6
'''
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if numero1 % numero2 == 0:
    print(numero1, "es multiplo de", numero2)
else:
    print(numero1, "no es multiplo de", numero2)

# Ejercicio 7

letra = input("Ingrese una letra: ")

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" or letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal")
else:
    print("Es una consonante")
'''
# Ejercicio 9
'''
dia = int(input("Ingrese un dia: "))

if dia == 1:
    print("El dia", dia, "es lunes")
elif dia == 2:
    print("El dia", dia, "es martes")
elif dia == 3:
    print("El dia", dia, "es miercoles")
elif dia == 4:
    print("El dia", dia, "es jueves")
elif dia == 5:
    print("El dia", dia, "es viernes")
elif dia == 6:
    print("El dia", dia, "es sabado")
elif dia == 7:
    print("El dia", dia, "es domingo")
else:
    print("El dia", dia, "no es valido")
'''
# Ejercicio 10
'''
hora1 = int(input("Ingrese la hora: "))
minuto1 = int(input("Ingrese el minuto: "))
segundo1 = int(input("Ingrese el segundo: "))

hora2 = int(input("Ingrese la hora: "))
minuto2 = int(input("Ingrese el minuto: "))
segundo2 = int(input("Ingrese el segundo: "))

tiempo1 = hora1, minuto1, segundo1
tiempo2 = hora2, minuto2, segundo2

if tiempo1 > tiempo2:
    print("Hora:" ,str(hora1),':', str(minuto1),':', str(segundo1), "es mayor")
elif tiempo1 < tiempo2:
    print("Hora 2:" ,str(hora2),":", str(minuto2),":", str(segundo2), "es mayor")
else:
    print("Tiempos iguales")
'''
# Ejercicio 14
'''
anio = int(input("Dime un año: "))
mes = int(input("Dime un mes (1-12): "))
dia = int(input("Dime un dia (1-31): "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    if mes == 2 and dia <= 29:
        print("La fecha es valida en el año bisiesto")
    else:
        print("Febrero no tiene mas de 29 dias en un año bisiesto")
elif mes == 2 and dia <= 28:
    print("La fecha es valida en un año no bisiesto")
else:
    print("Febrero no tiene mas de 28 dias en un año no bisiesto")
'''

# Ejercicio 16
'''
angulo1 = int(input("Ingrese un angulo: "))
angulo2 = int(input("Ingrese otro angulo: "))
angulo3 = int(input("Ingrese otro angulo: "))

if angulo1 + angulo2 > angulo3 and angulo1 + angulo3 > angulo2 and angulo2 + angulo3 > angulo1:
    if angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
        print("Es un triangulo equilateral")
    elif angulo1 == angulo3 and angulo1!=angulo3!=angulo2:
        print("Es un triangulo isosceles")
    elif angulo1 != angulo2 and angulo1 != angulo3 and angulo2 != angulo3:
        print("Es un triangulo escalar")
    elif angulo1 + angulo2 == angulo3 or angulo1 + angulo3 == angulo2 or angulo2 + angulo3 == angulo1:
        print("Es un triangulo right")
else:
    print("No es un triangulo")
'''
# Ejercicio 17
'''
numero3 = int(input("Ingrese un numero: "))
nummero4 = int(input("Ingrese otro numero: "))

if numero3 > nummero4:
    print (numero3 - nummero4)
else:
    print (nummero4 - numero3)
'''

# Ejercicio 19


llamada = int(input("Cuanto ha durado tu llamada (en minutos) "))
dia = input("Dia de la semana: ")
hora = int(input("Hora de la llamada (0-23): "))

if llamada <= 10:
    if dia != "D" and hora <= 12:
         print(((llamada * 0.66) * 15) / 100 + (llamada * 0.66))
    elif dia != "D" and hora >= 12:
        print(((llamada * 0.66) * 10) / 100 + (llamada * 0.66))
    else:
        print(((llamada * 0.66) * 3) / 100 + (llamada * 0.66))
elif llamada <= 13:
    if dia != "D" and hora <= 12:
        print(((llamada * 0.66) * 15) / 100 + (llamada * 0.66))
    elif dia != "D" and hora >= 12:
        print(((llamada * 0.66) * 10) / 100 + (llamada * 0.66))
    else:
        print(((llamada * 0.66) * 3) / 100 + (llamada * 0.66))
elif llamada <= 15:
    if dia != "D" and hora <= 12:
        print(((llamada * 0.66) * 15) / 100 + (llamada * 0.66))
    elif dia != "D" and hora >= 12:
       print(((llamada * 0.66) * 10) / 100 + (llamada * 0.66))
    else:
        print(((llamada * 0.66) * 3) / 100 + (llamada * 0.66))
elif llamada > 15:
    if dia != "D" and hora <= 12:
        print(((llamada * 0.66) * 15) / 100 + (llamada * 0.66))
    elif dia != "D" and hora >= 12:
        print(((llamada * 0.66) * 10) / 100 + (llamada * 0.66))
    else:
        print((((llamada * 0.66) * 3) / 100) + (llamada * 0.66))