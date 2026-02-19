import re


def menu():
    lista = ["Marca uno de los siguientes numeros: ","1. Llenas tanque (diesel o gasolina)", "2. Asignar coche al surtidor y repostar", "3. Consultar puntos de clientes", "4. Comprobar historicos de ventas", 
            "5. Consultar el estado de los surtidores", "6. Asignar precio a la gasolina/diesel", "7. Cerrar el programa y salir"]
    for i in lista:
        print(i)

def opcion1(surtidores):
    cantidad = int(input("cantidad a añadir al tanque: "))
    surtidor = int(input("¿A que surtidor? 1, 2, 3 o 4: "))
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
    nuevo = True
    pagos = False
    acumulador = []
    clientes = [['5555KKK', 'gasolina', 10], ['6666LLL', 'diesel', 20]]
    surtidores = [5000, 5000, 5000, 5000]
    combustible_distribuido = [0, 0 ,0, 0]


    matricula = input("Introduce la matricula de tu coche: ")

    #Comprueba que sea una matricula valida
    while not re.match(r'^[1-9]{4}[A-Z]{3}$', matricula):
        matricula = input("Introduce una matricula valida: ")

    #Comprueba si el cliente ya existe
    for i in clientes:
        if matricula in i:
            nuevo = False


    #Si es un nuevo cliente pregunta por que tipo de combustible usa y cuanto paga
    if nuevo == True:
        combustible = input("Introduce el tipo de combustible (gasolina o diesel): ")
        while combustible != "gasolina" and combustible != "diesel":
            combustible = input("Introduce un tipo de combustible valido (gasolina o diesel): ")
        pago = input("Introduce cuanto vas a pagar: ")
        while not re.match(r'^\d+(\.\d{1,2})?$', pago):
            pago = float(input("Introduce un pago valido con 2 decimales: "))
            
    #Los datos se añaden a la lista de clientes
        acumulador.insert(0, matricula)
        acumulador.insert(1, combustible)
        acumulador.insert(2, pago)
        clientes.append(acumulador)

    #Si es un cliente existente pregunta por cuanto paga
    else:
        pago = input("Introduce cuanto vas a pagar: ")
        while not re.match(r'^\d+(\.\d{1,2})?$', pago):
            pago = float(input("Introduce un pago valido con 2 decimales: "))
            
    #Suma el pago a los datos del cliente
        for i in range(len(clientes)):
            if clientes[i][0] == matricula:
                clientes[i][2] = float(clientes[i][2]) + float(pago)
        
    # Para comprobar por que surtidor tiene que pasar el cliente
    for i in range(len(clientes)):
    
    # Busco a que cliente corresponder la matricula
        if clientes[i][0] == matricula:
            for j in clientes[i]:

                #Compruebo que combustible usa
                if j[1] == 'gasolina':
                    if combustible_distribuido[0] < combustible_distribuido[1]:
                        print(f"Pase por el distribuidor 1")
                        combustible_distribuido[0] += float(pago)
                        surtidores[0] -= float(pago)
                    else:
                        print(f"Pase por el distribuidor 2")
                        combustible_distribuido[1] += float(pago)
                        surtidores[1] -= float(pago)
                else:
                    if combustible_distribuido[2] < combustible_distribuido[3]:
                        print(f"Pase por el distribuidor 3")
                        combustible_distribuido[2] += float(pago)
                        surtidores[2] -= float(pago)
                    else:
                        print(f"Pase por el distribuidor 4")
                        combustible_distribuido[3] += float(pago)
                        surtidores[3] -= float(pago)

def opcion3():
    clientes = [['5555KKK', 'gasolina', 63], ['6666LLL', 'diesel', 20]]
    valido = False

    matricula = input("Introduce la matricula de tu coche: ")
    while not re.match(r'^[1-9]{4}[A-Z]{3}$', matricula):
        matricula = input("Introduce una matricula valida: ")

    for i in clientes:
        if matricula in i:
            pago = i[2]
            valido = True

    if valido == True:
        puntos = int(pago) // 20
        print(f"El pago de {matricula} es de {puntos} puntos")
    else:
        print("No es un cliente de nuestra gasolinera")

def opcion4():
    clientes = [['5555KKK', 'gasolina', 63], ['6666LLL', 'diesel', 20]]

    for i in clientes:
        print(f"Matricula: {i[0]}, Combustible: {i[1]} y Puntos: {i[2]}")

def opcion5():
    combustible_distribuido = [123, 212314, 1243, 473564534]

    surtidor = int(input("Introduce el numero de surtidor (1, 2, 3 o 4): "))

    while surtidor < 1 or surtidor > 4:
        surtidor = int(input("Introduce un surtidor valido: "))
    
    print(combustible_distribuido[surtidor - 1])

def opcion6():
    precio_gasolina = float(input("Introduce el precio de gasolina: "))
    precio_diesel = float(input("Introduce el precio de diesel: "))

    precio_maximo = precio_gasolina * 0.2
    precio_minimo = precio_gasolina * 0.8

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