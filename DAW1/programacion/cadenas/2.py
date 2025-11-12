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