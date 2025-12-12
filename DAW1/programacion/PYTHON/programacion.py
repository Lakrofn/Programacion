# Ejercios de google 1

# Ejercicio 1 

edad = int(input("Cuantos años tienes"))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2

contra1 = input("Escriba una contraseña")
contra2 = input("Vuelva a escribir la contraseña")

contraseña = contra1

if contra2 == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta la contraseña deberia de haber sido: ",contraseña)

#Ejercicio 3

num1 = int(input("Ingrese un numero"))
num2 = int(input("Ingrese otro numero"))

if num1 // num2 == 0:
    print("ERROR")
else:
    print(num1 // num2)

#Ejercicio 4

num3 = int(input("Ingrese un numero"))

if num3 % 2 == 0:
    print("Es par")
else:
    print("Es impar")

#Ejercicio 5

edad1 = int(input("Ingrese una edad"))
ingreso = int(input("Ingrese un ingreso"))

if edad1 >= 16 and ingreso >= 1000:
    print(" puede tributar")
else:
    print(" no puede tributar")

#Ejercicio 6

nombre = input("Ingrese su nombre")
genero = input("Genero")

if ((genero == "M" or genero == "m") and nombre > "M") and ((genero == "H" or genero == "h") and nombre < "N"):
    print("Eres del grupo A")
else:
    print("Eres del grupo B")

# Ejercicio 7

renta = int(input("Ingrese su renta"))

if renta <=10000:
    print("5% de su renta")
elif renta > 100000 and renta <= 200000:
    print("15% de su renta")
elif renta > 200000 and renta <= 350000:
    print("20% de su renta")
elif renta > 350000 and renta <= 600000:
    print("30% de su renta")
else:
    print("45% de su renta")

# Ejercicio 8
