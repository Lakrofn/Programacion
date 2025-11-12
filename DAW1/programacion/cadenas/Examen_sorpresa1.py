def validardni(dni):
   if len(dni) < 0 or len(dni) > 9:
       return False
   abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   letra = ""
   numeros= "1234567890"
   acumulador = ""


   if len(dni) == 9:
       for i in dni:
           if i in abecedario:
               letra += i
           elif i in numeros:
               acumulador += i
           else:
               return False
   if len(dni) == 8:
       for i in dni:
           if i == 8 and i in abecedario:
               letra += i
           elif i in numeros:
               acumulador += i
           else:
               return False
  
   letraactual = input("Que letra tiene tu dni")
   letranumero = int(input("que numero le corresponde a tu dni"))


   if int(acumulador) % 23 == letranumero:
       return True
  


assert(validardni("47429121Q"))