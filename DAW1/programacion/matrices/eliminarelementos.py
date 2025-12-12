lista = [[1,3,5,7,9],[2,4,6,8,10, "ana", 4,4 ,42, 10]]

acumulador = 0

for i in lista[1]:
    if i == 4:
        acumulador += 1

while acumulador != 0:
    lista[1].remove(4)
    acumulador -= 1
    
print (lista)