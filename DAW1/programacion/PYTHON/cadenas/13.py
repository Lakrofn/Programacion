def reemplazar_palabra(cadena, busca, reemplazo):
   palabra = ""
   acumulador = ""
   for i in cadena:
       if i != " ":
           palabra += i
           if palabra.lower() == busca.lower():
               palabra = reemplazo
               acumulador += palabra
               palabra = ""
       elif i == " ":
           acumulador += palabra + " "
           palabra = ""
   acumulador += palabra

   return acumulador

assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "Hola", "Adrian") == "Adrian soy Alvaro y tengo 23 años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "soy", "Adrian") == "Hola Adrian Alvaro y tengo 23 años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "Alvaro", "Adrian") == "Hola soy Adrian y tengo 23 años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "y", "Adrian") == "Hola soy Alvaro Adrian tengo 23 años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "tengo", "Adrian") == "Hola soy Alvaro y Adrian 23 años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "23", "Adrian") == "Hola soy Alvaro y tengo Adrian años")
assert(reemplazar_palabra("Hola soy Alvaro y tengo 23 años", "años", "Adrian") == "Hola soy Alvaro y tengo 23 Adrian")
