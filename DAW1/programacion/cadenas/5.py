def caracterenstring(frase, caracter):
   contador = 0
   for i in frase:
       if i == caracter:
           contador += 1
   return contador


print(caracterenstring("Hola soy alvaro, me gusta entrenar calistenia y mma","a"))