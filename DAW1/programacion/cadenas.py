# Ejercicio 1
'''
cadena = ("HolA soy AlvaRo CrUces MartInez")
abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


palabra = ""
acumulador = ""




for letra in cadena:
  palabra += letra
  if letra == " ":
      if palabra[0] in abecedario:
          acumulador += palabra[0]
      palabra = ""
if palabra[0] in abecedario:
  acumulador += palabra[0]




print(acumulador)
'''
# Ejercicio 2
'''
cadena = ("Hola soy alvaro cruces martinez")

palabra = ""
palabrafinal = ""

acumulador = ""
for espacio in cadena:
  if espacio != " ":
      palabra += espacio
   
  else:
      for i in range(len(palabra)):
          if i == 0:
              palabrafinal += palabra[0].upper()
          else:
              palabrafinal += palabra[i]
      acumulador += palabrafinal
      palabra = ""
      palabrafinal = ""

for i in range(len(palabra)):
    if i == 0:
        palabrafinal += palabra[0].upper()
    else:
        palabrafinal += palabra[i]
acumulador += palabrafinal

print (acumulador)
'''
# Ejercicio 3
'''
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
'''
# Ejercicio 5
'''
def caracterenstring(frase, caracter):
  contador = 0
  for i in frase.lower():
      if i == caracter:
          contador += 1
  return contador

print(caracterenstring("Hola soy Alvaro, me gusta entrenar calistenia y jugar videojuegos","a"))
'''
# Ejercicio 6
'''
def lowcaseinstring(frase, caracter):
  abecedario = "abcdefghijklmnopqrstuvwxyz"
  contador = 0
  for i in frase:
      if i == caracter and i in abecedario:
          contador += 1
  return contador


print(lowcaseinstring("HolA soy Alvaro Cruces Martinez, me gusta entrenAr calisteniA y jugar videojuegos","a"))
'''
# Ejercicio 7
'''
def numeroenfrase(frase):
  numero = "1234567890"
  contador = 0
  for i in frase:
      if i in numero:
          contador += 1
  return contador


print(numeroenfrase("H0l4 s0y 4lvar0 6ruce2 mart1ne7, m3 gu27a 3ntren4r 6alisteni9"))
'''
# Ejercicio 8
'''
def palindromo(cadena):
    acumulador = ""
    for i in cadena:
        if i != " ":
            acumulador += i.lower()

    if acumulador == acumulador.lower()[::-1]:
        return True
    else:
        return False

print(palindromo("se es o no se es"))
'''
# Ejercicio 9
'''
def palabra_escondida(cadena, palabra):
   reduccion = palabra.lower()
   resultado = ""
   for i in cadena:
       while len(reduccion) > 0 and reduccion[0] in i:
           resultado += i
           reduccion = reduccion[1:]
     
   if resultado == palabra:
       return True
   else:
       return False
 
print(palabra_escondida("supercalifragilisticoespialidoso","rapido"))
'''
# Ejercicio 10
'''
def armstrongnumber(numero):
  contador = 0
  suma = 0
  for i in numero:
      contador += 1
  for j in numero:
      suma += int(j) ** contador
  if suma == int(numero):
      return print("Es un numero Armstrong")
  else:
      return print("No es un numero Armstrong")     


armstrongnumber("371")
'''
# Ejercicio 11
'''
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
'''
# Ejercicio 12
'''
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
'''
# Ejercicio 13
'''
def palabra_escondida(cadena, palabra, reemplazo):
   reduccion = palabra.lower()
   reduccionreemplazo = reemplazo.lower()
   cadenanueva = ""
   for i in cadena:
       while len(reduccion) > 0 and len(reduccionreemplazo) > 0 and reduccion[0] in i:
           i = reduccionreemplazo[0]
           reduccion = reduccion[1:]
           reduccionreemplazo = reduccionreemplazo[1:]
       cadenanueva += i
   return cadenanueva

print(palabra_escondida("supercalifragilisticoespialidoso","rapido", "veloz"))
'''
'''
def reemplazar_palabra(cadena, busca, reemplazo):
   cadena = str.lower(cadena)
   palabra = ""
   acumulador = ""
   for i in cadena:
       if i != " ":
           palabra += i
           if palabra == busca:
               palabra = reemplazo
               acumulador += palabra
               palabra = ""
       elif i == " ":
           acumulador += palabra + " "
           palabra = ""
   acumulador += palabra

   return acumulador

print(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "alvaro", "adrian"))
'''
# Ejercicio 14
'''
def reemplazar_palabra(cadena, busca, reemplazo, veces):
   cadena = str.lower(cadena)
   palabra = ""
   acumulador = ""
   reemplazoacumulado= ""
   for i in cadena:
       if i != " ":
           palabra += i
           if palabra == busca:
               for j in range(1,veces + 1):
                   if j < veces:
                       reemplazoacumulado += reemplazo + " "
                   else:
                       reemplazoacumulado += reemplazo
               palabra = reemplazoacumulado
               acumulador += palabra
               palabra = ""
       elif i == " ":
           acumulador += palabra + " "
           palabra = ""
   acumulador += palabra


   return acumulador

print(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "alvaro", "adrian", 4))
'''
# Ejercicio 15
'''
def contar_vocales(cadena):
   palabra = ""
   vocales = "aeiouAEIOU"
   acumulador = 0
   for i in cadena:
       if i in vocales:
           if i not in palabra:
               palabra += i.lower()
               acumulador += 1
   return acumulador

print(contar_vocales("Alvaro"))
'''
# Ejercicio 16
'''
def contar_consonantes(cadena):
   palabra = ""
   vocales = "aeiouAEIOU"
   acumulador = 0
   for i in cadena:
       if i not in vocales:
           if i not in palabra:
               palabra += i.lower()
               acumulador += 1
   return acumulador


print(contar_consonantes("Alvaro"))
'''
# Ejercicio 17
'''
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
'''
# Ejercicio 18
'''
def contar_palabras(cadena):
   contador = 1
   for i in cadena:
       if i == " ":
           contador += 1
   return contador

print(contar_palabras("Hola soy Alvaro Cruces Martinez, me gusta entrenar calistenia y jugar videojuegos"))
'''
# examen
'''
def validardni(dni):
  if len(dni) < 0 or len(dni) > 9:
      return False
  abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letra = ""
  numeros= "1234567890"
  acumulador = ""

  if len(dni) == 9:
      for i in dni:
          if i in abecedario:
              letra += i
          elif i in numeros:
              acumulador += i
          else:
              return False
  if len(dni) == 8:
      for i in dni:
          if i == 8 and i in abecedario:
              letra += i
          elif i in numeros:
              acumulador += i
          else:
              return False
  letraactual = input("Que letra tiene tu dni")
  letranumero = int(input("que numero le corresponde a tu dni"))

  if int(acumulador) % 23 == letranumero:
      return True

assert(validardni("47429121Q"))
'''

