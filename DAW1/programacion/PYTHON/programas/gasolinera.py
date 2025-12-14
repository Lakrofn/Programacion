import re


def menu():
    lista = ["Marca uno de los siguientes numeros: ","1. Llenas tanque (diesel o gasolina)", "2. Asignar coche al surtidor y repostar", "3. Consultar puntos de clientes", "4. Comprobar historicos de ventas", 
            "5. Consultar el estado de los surtidores", "6. Asignar precio a la gasolina/diesel", "7. Cerrar el programa y salir"]
    for i in lista:
        print(i)

def opcion1(surtidores):
    cantidad = int(input("cantidad a añadir al tanque: "))
    surtidor = int(input("Al sirtidor 1, 2, 3 o 4: "))
    while surtidor < 0 or surtidor > 4 or cantidad < 0:
        if surtidor < 0 or surtidor > 4:
            print("Numero de surtidor incorrecto")
            surtidor = int(input("Selecciona entre el surtidor 1, 2, 3 o 4: "))
        elif cantidad < 0:
            print("Cantidad incorrecta")
            cantidad = int(input("Introduce cantidad a añadir al tanque valida: "))
    
    for i in range (len(surtidores)):
        if surtidor - 1 == i:
            if surtidores[i] + cantidad <= 5000:
                surtidores[i] += cantidad  
            else:
                surtidores[i] = 5000
            print(f"El sustidor {surtidor} esta con {surtidores[i]} litros")

def opcion2():
    decimales = ""
    nuevo = True
    pagos = False
    acumulador = []
    clientes = [['5555KKK', 'gasolina', 10], ['6666LLL', 'diesel', 20]]
    surtidores = [5000, 5000, 5000, 5000]
    combustible_distribuido = [0, 0 ,0, 0]
    matricula = input("Introduce la matricula de tu coche: ")
    while not re.match(r'^[1-9]{4}[A-Z]{3}$', matricula):
        matricula = input("Introduce una matricula valida: ")

    for i in clientes:
        if matricula in i:
            nuevo = False
    if nuevo == True:
        combustible = input("Introduce el tipo de combustible (gasolina o diesel): ")
        while combustible != "gasolina" and combustible != "diesel":
            combustible = input("Introduce un tipo de combustible valido (gasolina o diesel): ")
        while pagos == False:
            pago = float(input("Introduce un pago valido con 2 decimales: "))
            decimales = str(pago[-3:])
            if len(decimales) == 2:
                pagos = True

        acumulador.append(matricula)
        acumulador.append(combustible)
        acumulador.append(pago)
        clientes.append(acumulador)
    else:
        pago = float(input("Introduce cuanto vas a pagar: "))
        while pagos == False:
            pago = float(input("Introduce un pago valido con 2 decimales: "))
            decimales = str(pago[-3:])
            if len(decimales) <= 2:
                pagos = True

        for i in clientes:
            if i[0] == matricula:
                for j in i:
                    if j.isdigit():
                        clientes[i][j] += pago
        
    
    for i in clientes:
        if i[0] == matricula:
            for j in i:
                if j[1] == "gasolina":
                    if combustible_distribuido[0] < combustible_distribuido[1]:
                        print(f"Pase por el distribuidor 1")
                        combustible_distribuido[0] += pago
                        surtidores[0] -= pago
                    else:
                        print(f"Pase por el distribuidor 2")
                        combustible_distribuido[1] += pago
                        surtidores[1] -= pago
                else:
                    if combustible_distribuido[2] < combustible_distribuido[3]:
                        print(f"Pase por el distribuidor 3")
                        combustible_distribuido[2] += pago
                        surtidores[2] -= pago
                    else:
                        print(f"Pase por el distribuidor 4")
                        combustible_distribuido[3] += pago
                        surtidores[3] -= pago

opcion2()

def gasolinera():
    importe = 0
    clientes = []
    surtidores = [5000, 5000, 5000, 4990]
    combustible_distribuido = [0, 0, 0, 0]

    menu()
    opcion = int(input("Marca un numero: "))
    while opcion < 1 or opcion > 7:
        opcion = int(input("Introduce un numero valido: "))
    while opcion != 7:
        if opcion == 1:
            opcion1(surtidores)

        elif opcion == 2:
            opcion2(clientes, surtidores, combustible_distribuido)
        

        menu()
        opcion = int(input("Marca otro numero: "))




#gasolinera()