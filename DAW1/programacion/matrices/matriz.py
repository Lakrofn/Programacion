matriz = [[5,0,0], [0,9,0], [0,0,7]]
acumulador = ""


for i in matriz:
    for j in i:
        acumulador += " " + str(j)
    print (acumulador)
    acumulador = ""