# Boletin de ejercicios 1
# Ejercicio 1
'''
num1 = int(input("Dime un numero "))
num2 = int(input("Dime otro numero "))

# Con for
if num1 < num2:
   for i in range(num1, num2 + 1):
       print(i)
else:
   for b in range(num2 , num1 + 1):
       print(b)

# Con while
while num1 < num2 or num1 > num2:
   if num1 != num2 and num1 < num2:
       print (num1)
       num1 += 1
   elif num1 != num2 and num1 > num2:
       print (num2)
       num2 += 1

print(num1)
'''
# Ejercicio 2
'''
num1 = int(input("Dime un numero"))

multiplo = 0

# Con while
while multiplo <= 10:
   print (num3, "por" ,multiplo, "=" ,num3 * multiplo)
   multiplo += 1

#con for
for multiplo in range(11):
   print (num3, "por" ,multiplo, "=" ,num3 * multiplo)
'''
# Ejercicio 3
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

# Con for
for i in range(num1, num2):
   if i % 11 == 0:
       print(i, "es un multiplo de 11")

# Con while
while num1 != num2:
   while num1 < num2:
       if num1 % 11 == 0:
           print(num1, "es un multiplo de 11")
       num1 += 1
   while num2 < num1:
       if num2 % 11 == 0:
           print(num2, "es un multiplo de 11")
       num2 += 1
'''
# Ejercicio 4
'''
num1 = int(input("Ingrese un numero: "))

contador = 0
maxima = 0
media = 0

# Con while
while 0<=num1<=10000:
   contador += 1
   media += num1
   if num1 > maxima:
       maxima = num1
   num1 = int(input("Introduzca otro numero: "))

# Con for
for i in range(0,10001):
   num1 = int(input("Introduzca otro numero: "))
   if 0<=num1<=10000:
       contador += 1
       media += num1
       if num1 > maxima:
           maxima = num1
   else:
       break


print("El numero de numeros introducidos es:", contador)
print("La media es:", media/contador)
print("El maximo es:", maxima)
'''
# Ejercicio 5
'''
n = int(input("Introduce un numero: "))
suma = 0

while n < 0:
   n = int(input("No es un numero positivo introduzca otro: "))

# Con for
for i in range(1,n + 1):
   suma += i

print (suma)

# Con while
i = 0

while n >= i:
   suma += i
   i += 1
print (suma)

# Sin bucles
if n <= 0:
   ("El numero no es positivo")
else:
   print (n * (n + 1) // 2)
'''
# Ejercicio 6
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

resultado = 0

while num1 < 0 or num2 < 0:
   num1 = int(input("Ingrese un numero positivo: "))

# Con for
if num1 < num2:
   for suma in range(num1, num2 + 1):
       resultado += suma
else:
   for suma in range(num2, num1 + 1):
       resultado += suma
print (resultado)

# Con while
if num1 < num2:
   while num1 <= num2:
       resultado += num1
       num1 += 1
else:
   while num2 <= num1:
       resultado += num2
       num2 += 1
print (resultado)

# Sin bucles
print((num1 * (num1 - 1) // 2) + (num2 * (num2 + 1) // 2))
'''
# Ejercicio 7
'''
num1 = int(input("Ingrese un numero: "))

maximo = 0

# Con while
while num1 <= 100:
   if num1 > maximo:
       maximo = num1
   num1 = int(input("Introduzca otro numero: "))

# Con for
for i in range(101):
   num1 = int(input("Introduzca un numero: "))
   if i > maximo:
       maximo = i

print("El numero maximo es:", maximo)
'''
# Ejercicio 8
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

contador = 0
resultado = 0

while contador < num2:
   resultado += num1
   contador += 1

if (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0):
   resultado = -resultado

print("El producto es " ,resultado)
'''
# Ejercicio 9
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

mayor = num2
menor = num1

suma = 0
acumulador = 0

if num1 > num2:
   mayor = num1
   menor = num2

while acumulador < mayor:
   suma += menor
   acumulador += menor

print("El modulo es ",suma - mayor)
'''
# Ejercicio 10
'''
num1 = int(input("Cuantos numeros positivos quieres pedir: "))

mayor = 0
menor = 0

for i in range(num1):
   num2 = int(input("Ingrese un numero positivo: "))
   while num2 < 0:
       num2 = int(input("Ingrese un numero positivo valido: "))
   if num2 > mayor:
       mayor = num2
   if num2 < menor:
       menor = num2

print("El mayor numero es:", mayor)
print("El menor numero es:", menor)
'''
# Ejercicio 11

altura = int(input("Ingrese la altura: "))

while altura < 0:
    altura = int(input("Ingrese una altura mayor a cero: "))

for i in range(1, altura):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

# Ejercicio 12
'''
num1 = int(input("Ingrese un numero: "))

divisor = 0

suma = 0

for divisores in range(1, num1):
    if num1 % divisores == 0:
        suma += divisores

while divisor != num1-1:
    divisor += 1
    if num1 % divisor == 0:
        suma += divisor

if num1 == suma:
    print("Es un numero perfecto")
else:
    print("No es un numero perfecto")
'''
# ejercicio 13
'''
num1 = int(input("Ingrese un numero: "))

division = 1
suma = 0

for acumulador in range(1, num1 + 1):
    suma+=division / acumulador

print(suma)
'''
# ejercicio 14
'''
altura = int(input("Ingrese la altura: "))

while altura < 0:
    altura = int(input("Ingrese una altura mayor a cero: "))

for i in range(1, altura):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
for i in range(altura, 0, -1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
'''
# ejercicio 15
'''
num1 = int(input("Ingrese el primer numero: "))

multiplicador = 1

for i in range(1, num1 + 1):
    multiplicador *= i

print(multiplicador)
'''