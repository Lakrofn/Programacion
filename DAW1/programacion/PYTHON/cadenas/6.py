def lowcaseinstring(frase):
   abecedario = "abcdefghijklmnopqrstuvwxyz"
   contador = 0
   for i in frase:
       if i in abecedario:
           contador += 1
   return contador


assert(lowcaseinstring("HolA soy Alvaro Cruces Martinez, me gusta entrenAr calisteniA y MMA") == 46)
assert(lowcaseinstring("Alvar CRUCES MARTINEZ") == 4)
assert(lowcaseinstring("ALVARO CRUCES MARTINEZ") == 0)
assert(lowcaseinstring("alvaro cruces martinez") == 20)