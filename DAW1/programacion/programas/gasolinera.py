import re


def menu():
    lista = ["Marca uno de los siguientes numeros: ","1. Llenas tanque (diesel o gasolina)", "2. Asignar coche al surtidor y repostar", "3. Consultar puntos de cliente", "4. Comprobar historicos de ventas", 
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

def opcion2(gasolina, diesel, surtidores):
    acumulable
    gasolina=[]
    diesel=[]
    surtidores = [5000, 5000, 5000, 5000]
    matricula = input("Introduce la matricula de tu coche: ")
    while not re.match(r'^[1-9]{4}[A-Z]{3}$', matricula):
        matricula = input("Introduce una matricula valida: ")

    if matricula not in gasolina and matricula not in diesel:
        combustible = input("Introduce el tipo de combustible (gasolina o diesel): ")
        while combustible != "gasolina" and combustible != "diesel":
            combustible = input("Introduce un tipo de combustible valido (gasolina o diesel): ")

        gasolina.append(matricula) if combustible == "gasolina" else diesel.append(matricula)
    else:
        pago = float(input("Introduce cuanto vas a pagar: "))
        while pago < 10 or not re.match(r'^\d+(\.\d{1,2})?$', str(pago)):
            pago = float(input("Introduce un pago valido con 2 decimales: "))
        

    



def gasolinera():
    importe = 0
    gasolina = []
    diesel = []
    surtidores = [5000, 5000, 5000, 4990]

    menu()
    opcion = int(input("Marca un numero: "))
    while opcion < 1 or opcion > 7:
        opcion = int(input("Introduce un numero valido: "))
    while opcion != 7:
        if opcion == 1:
            opcion1(surtidores)

        elif opcion == 2:
            opcion2(gasolina, diesel, surtidores)
        

        menu()
        opcion = int(input("Marca otro numero: "))




gasolinera()