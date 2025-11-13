def caracterenstring(frase, caracter):
   contador = 0
   for i in frase.lower():
       if i == caracter:
           contador += 1
   return contador


assert(caracterenstring("Hola soy Alvaro, me gusta entrenar calistenia y jugar videojuegos", "a") == 8)
assert(caracterenstring("Hola soy Alvaro, me gusta entrenar calistenia y jugar videojuegos", "e") == 6)
assert(caracterenstring("Hola soy Alvaro, me gusta entrenar calistenia y jugar videojuegos", "i") == 3)
assert(caracterenstring("Hola soy AlvarO, me gusta entrenar calistenia y jugar videojuegos", "o") == 5)
assert(caracterenstring("Hola soy Alvaro, me gusta entrenar calistenia y jugar videojuegos", "u") == 3)