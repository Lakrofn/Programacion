def numeroenfrase(frase):
   numero = "1234567890"
   contador = 0
   for i in frase:
       if i in numero:
           contador += 1
   return contador


print(numeroenfrase("H0l4 s0y 4lvar0 6ruce2 mart1ne7, m3 gu27a 3ntren4r MM4 y 6alisteni9"))