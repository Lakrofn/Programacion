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