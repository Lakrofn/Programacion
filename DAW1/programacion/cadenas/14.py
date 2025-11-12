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