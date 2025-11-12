# Ejercicio 1
'''
cadena = int(input("Introduce cuantas veces quieres repetir la cadena: "))
numero_suma = int(input("Introduce el numero de la suma: "))

acumulador = 0
suma = 0

for i in range(1, cadena + 1):
  acumulador = acumulador * 10 + numero_suma
  print(acumulador)
  suma += acumulador

print("la suma es", suma)
'''
# Ejercicio 2
'''
elige = input("escrie 2 para binario o 10 para decimal? ")

decimal = 1
binario = 0

if elige == "10":
   for i in range(1, 6):
       linea = ""
       for j in range(1, i + 1):
           linea = linea + str(decimal) + " "
           decimal += 1
       print(linea)
elif elige == "2":
    for i in range(1, 6):
        linea = ""
        for j in range(1, i + 1):
            fila = i
            columna = j
            linea += str((i + j - 1) % 2) + " "
            
            if fila % 2 == 0:
                if columna % 2 == 0:
                    binario = 1
                    linea += str(binario) + " "
                else:
                    binario = 0
                    linea += str(binario) + " "
            else:
                if columna % 2 == 0:
                    binario = 0
                    linea += str(binario) + " "
                else:
                    binario = 1 
                    linea += str(binario) + " "
                
        print(linea)
'''
# Ejercicio 3
'''
num1 = int(input("Ingrese un numero: "))
veces = int(input("Ingresa cuantas operaciones quieres realizar: "))

potencia = 1
negativo = 1

while num1 < 0:
  num1 = int(input("Ingrese un numero positivo: "))

for i in range(1, veces + 1):
  if negativo == 1:
      print (num1 ** potencia)
      negativo = 0
      potencia += 2
  else:
      print (-num1 ** potencia)
      negativo = 1
      potencia += 2
'''
# Ejercicio 4
'''
cadena = int(input("Introduce cuantas veces quieres repetir la cadena: "))
numero_suma = int(input("Introduce el numero de la suma: "))

serie = ""
acumulador = 0
suma = 0

for i in range(1, cadena + 1):
   if i < cadena:
       acumulador = acumulador * 10 + numero_suma
       suma += acumulador
       serie += str(acumulador) + " " + "+" + " "
   else:
       acumulador = acumulador * 10 + numero_suma
       suma += acumulador
       serie += str(acumulador)

print(serie, "=", suma)
'''
# Ejercicio 5
'''
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

multiplicador = 0
maximo = 0

while num1 < 0 or num2 < 0:
  if num1 < 0:
      num1 = int(input("Introduce un numero positivo: "))
  elif num2 < 0:
      num2 = int(input("Introduce un numero positivo: "))

while maximo != 10:
      if multiplicador * num2 < num1:
          multiplicador += 1
          maximo += 0
      else:
          print(multiplicador * num2)
          multiplicador += 1
          maximo += 1
'''
# Ejercicio 6
'''
num1 = int(input("Dime un número "))

acumulador = num1

while acumulador != 1:
  if acumulador % 2 == 0:
      print(acumulador // 2)
      acumulador = acumulador // 2
  elif acumulador % 2 != 0:
      print(acumulador * 3 + 1)
      acumulador = acumulador * 3 + 1
'''
# Ejercicio 7
'''
dia = int(input("Dime un dia (1-31): "))
mes = int(input("Dime un mes (1-12): "))
anio = int(input("Dime un año: "))

# Version todos los dias siguientes hasta el ultimo dia de 2025

while mes < 1 or mes > 12:
   mes = int(input("Dime un mes valido (1-12): "))
while dia < 1 or dia > 31:
   dia = int(input("Dime un dia valido (1-31): "))
while anio < 0 or anio > 2025:
   anio = int(input("Dime un año valido (0-2025): "))


if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
   for year in range(anio, 2026):
       for month in range(mes, 13):
           while month == 2 and dia <= 29:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           while (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and dia >= 1 and dia <= 31:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           while (month == 4 or month == 6 or month == 9 or month == 11) and dia >= 1 and dia <= 30:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           mes += 1
           dia = 1
       anio += 1
       mes = 1
else:
   for year in range(anio, 2026):
       for month in range(mes, 13):
           while month == 2 and dia <= 28:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           while (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and dia >= 1 and dia <= 31:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           while (month == 4 or month == 6 or month == 9 or month == 11) and dia >= 1 and dia <= 30:
               fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
               print(fecha)
               dia += 1
           mes += 1
           dia = 1
       anio += 1
       mes = 1
'''
# Verion dia siguiente solamente
'''
while (mes > 1 or mes < 12) and (dia > 1 or dia < 31) and (anio > 0 or anio < 2025):
    fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
    print("Fecha actual: ", fecha)
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        if mes == 2 and dia <= 29:
            diamax=29
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
            diamax=31
        else:
            diamax=30
    else:
        if mes == 2 and dia <= 28:
            diamax=28
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia <= 31:
            diamax=31
        else:
            diamax=30

    dia = dia + 1
    if dia > diamax:
        dia = 1
        mes = mes + 1
        if mes > 12:
            mes = 1
            anio = anio + 1
    fecha = str(dia) + "/" + str(mes) + "/" + str(anio)
    print("Dia siguiente: ", fecha)

    dia = int(input("Dime un dia valido (1-31): "))
    mes = int(input("Dime un mes valido (1-12): "))
    anio = int(input("Dime un año valido (0-2025): "))
'''

# Ejercicio 8
'''
longitud = int(input("Ingrese la longitud de la secuencia: "))

ultimo = 1
actual = 1

for secuencia in range(1, longitud + 1):
   suma = ultimo + actual
   ultimo = actual
   actual = suma
   print(suma)
'''
# Ejercicio 9
'''
anterior = 0
actual = 1

valor = 0

rango = 2

while valor < 1000:
   valor = 3 * actual + 2 * anterior
   anterior = actual
   actual = valor
   rango += 1

print("el rango es", rango)
print("el valor es", valor)
'''
# Ejercicio 10
'''
edad = int(input("Ingrese un año: "))

puzzle = 0
ingreso = 0
dinero = 0

for year in range(1, edad + 1):
   if year <= 2:
       if year % 2 == 0:
           ingreso += 20
           dinero += ingreso
       else:
           puzzle += 1
   elif year % 2 == 0:
       ingreso += 15
       dinero += ingreso
   else:
       puzzle = puzzle * 2 + 1

print(f"Ha recibido {dinero} euros y {puzzle} puzzles")
'''
# Ejercicio 11
'''
figura = input("Ingrese una figura (cuadrado, triángulo o rombo): ")

n = 1
m = 5

if figura == "cuadrado" or figura == "Cuadrado":
   for i in range(1, 5):
       if i == 1 or i == 4:
           print(("*" + " ") * 4)
       else:
           print("*" + (" " * 5) + "*")
elif figura == "triangulo" or figura == "Triangulo":
   for i in range(1, 5):
       if i == 1:
           espacios = " " * (4 - i)
           print(espacios + "*")
       elif i == 4:
           print("*" * (i * 2 - 1))
       else:
           espacios = " " * (4 - i)
           medio = " "
           asteriscos = "*" + (medio * n) + "*"
           n += 2
           print(espacios + asteriscos)
elif figura == "rombo" or figura == "Rombo":
   for i in range(1, 5):
       if i == 1:
           espacios = " " * (4 - i)
           print(espacios + "*")
       else:
           espacios = " " * (4 - i)
           medio = " "
           asteriscos = "*" + (medio * n) + "*"
           n += 2
           print(espacios + asteriscos)
   for i in range(3, 0, -1):
       if i == 1:
           espacios = " " * (4 - i)
           print(espacios + "*")
       else:
           m -= 2
           espacios = " " * (4 - i)
           medio = " "
           asteriscos = "*" + (medio * m) + "*"
           print(espacios + asteriscos)
'''
# Ejercicio 12
'''
num1 = int(input("Introduce un número: "))
area = 2 * num1 - 1

for i in range(area):
    linea = ""

    for j in range(area):
        arriba = i
        izquierda = j
        abajo = area - 1 - i
        derecha = area - 1 - j

        menor = arriba
        if izquierda < menor:
            menor = izquierda
        if abajo < menor:
            menor = abajo
        if derecha < menor:
            menor = derecha

        valor = num1 - menor

        linea += str(valor) + " "
    
    print(linea)
'''