def avescapturadas():
    campanias = int(input("Cuantas capañas han habido? "))
    total = ""
    while campanias > 0:
        total += str(campanias) + "\n"
        suma = 0
        for i in range(campanias):
            capturadas = int(input("Cuantas aves has capturado para la capaña " + str(i+1) + "? "))
            anilladas = int(input("Cuantas aves estaban anilladas para la capaña " + str(i+1) + "? "))
            total += str(capturadas) + " " + str(anilladas) + "\n"
            suma += capturadas - anilladas
        total += str(suma) + "\n"
        campanias = int(input("Cuantas capañas han habido? "))
    print(total[:-1])

avescapturadas()