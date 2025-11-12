def lowcaseinstring(frase, caracter):
   abecedario = "abcdefghijklmnopqrstuvwxyz"
   contador = 0
   for i in frase:
       if i == caracter and i in abecedario:
           contador += 1
   return contador


print(lowcaseinstring("HolA soy Alvaro Cruces Martinez, me gusta entrenAr calisteniA y MMA","a"))