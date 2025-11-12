def armstrongnumber(numero):
   contador = 0
   suma = 0
   for i in numero:
       contador += 1
   for j in numero:
       suma += int(j) ** contador
  
   return suma == int(numero)      


assert(armstrongnumber("371") == True)
assert(armstrongnumber("123") == False)
assert(armstrongnumber("10") == False)
assert(armstrongnumber("1") == True)
assert(armstrongnumber("407") == True)