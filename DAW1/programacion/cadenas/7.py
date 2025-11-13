def numeroenfrase(frase):
   numero = "1234567890"
   contador = 0
   for i in frase:
       if i in numero:
           contador += 1
   return contador


assert(numeroenfrase("H0l4 s0y 4lvar0 6ruce2 mart1ne7, m3 gu27a 3ntren4r MM4 y 6alisteni9") == 17)
assert(numeroenfrase("alvaro CRUCES martinez") == 0)
assert(numeroenfrase("4lvar0 6ruce2 8ar5ine7") == 7)