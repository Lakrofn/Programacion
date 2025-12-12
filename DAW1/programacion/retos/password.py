
def password(numero):
    lista = ['L68', 'L30','R48','L5','R60','L55','L1','L99','R14','L82',]
    archivo = open("/users/alvar/Desktop/numeros.txt")
    password = 0
    for linea in lista:
        indicacion = linea.replace("\n", "")
        if indicacion[0] == 'R':
            movimiento = int(indicacion[1:])
            while movimiento > 0:
                if numero != 100:
                    numero += 1
                    movimiento -= 1
                else:
                    password += 1
                    movimiento -= 1
                    numero = 0
        else:
            movimiento = int(indicacion[1:])
            while movimiento > 0:
                if numero != 0:
                    numero -= 1
                    movimiento -= 1
                else:
                    password += 1
                    movimiento -= 1
                    numero = 99

        
    print (password)

password(50)