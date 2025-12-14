
def password(numero):
    archivo = open("/users/alvar/Desktop/numeros.txt")
    password = 0
    for linea in archivo:
        indicacion = linea.replace("\n", "")
        if indicacion[0] == 'R':
            movimiento = int(indicacion[1:])
            while movimiento > 0:
                numero += 1
                movimiento -= 1
                if numero == 100:
                    numero = 0
                    password += 1
                    movimiento -= 1
            if numero == 100:
                numero = 0
                password += 1
        else:
            movimiento = int(indicacion[1:])
            while movimiento > 0:
                numero -= 1
                movimiento -= 1
                if numero == 0:
                    numero = 100
                    password += 1
            if numero == 0:
                numero = 100
                password += 1

        
    print (password)

password(0)