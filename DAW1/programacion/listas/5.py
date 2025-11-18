import random

def domino():
    # Estas variables son para almacenar las fichas
    fichas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
    jugador1 = []
    jugador2 = []
    movimiento = []
    contador = 0

    # Estas variables es para comprobar las fichas que se encuentran en cada extremo
    ultima_ficha = []
    primera_ficha = []

    # Esta variable indica la partida actual
    jugadas =[]

    # Fichas para el jugador 1
    while contador < 7:
        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
        jugador1.append(movimiento)
        movimiento = []
        contador += 1
    contador = 0

    #Fichas para el jugador 2
    while contador < 7:
        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
        jugador2.append(movimiento)
        movimiento = []
        contador += 1
    contador = 0
    
    doble_mas_alta1 = []
    doble_mas_alta2 = []
    doble_actual = []

    # comprobamos quien empieza primero
    for i in jugador1:
        if i[0] == i[1]:
            doble_actual.append(i)
            if doble_actual > doble_mas_alta1:
                doble_mas_alta1 = doble_actual
        doble_actual = []
    for i in jugador2:
        if i[0] == i[1]:
            doble_actual.append(i)
            if doble_actual > doble_mas_alta2:
                doble_mas_alta2 = doble_actual
        doble_actual = []

    # Comprobamos quien gana
    if doble_mas_alta1 > doble_mas_alta2:
        print(f"El jugador 1 gana con {doble_mas_alta1[0]}")
        jugadas.append(doble_mas_alta1[0])
        jugador1.remove(doble_mas_alta1[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta1[0]
        primera_ficha = doble_mas_alta1[0]

        # comprobamos si el jugador 1 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
        if len(fichas) != 0:
            while ultima_ficha[1] not in jugador2 or ultima_ficha[2] not in jugador2 or primera_ficha[1] not in jugador2 or primera_ficha[2] not in jugador2:
                print(f"jugador 2 roba una ficha a no tener ninguna ficha compatible")
                movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                jugador2.append(movimiento)
                movimiento = []
        else:
            print(f"Jugador 2 pasa al no tener fichas")
        eleccion = input(f"Jugador 2 elige una de tus siguientes fichas: {jugador2}")
    elif doble_mas_alta2 > doble_mas_alta1:
        print(f"El jugador 2 gana con {doble_mas_alta2[0]}")
        jugadas.append(doble_mas_alta2[0])
        jugador2.remove(doble_mas_alta2[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta2[0]
        primera_ficha = doble_mas_alta2[0]

        # comprobamos si el jugador 1 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
        if len(fichas) != 0:
            while ultima_ficha[0] not in jugador1 or ultima_ficha[1] not in jugador1 or primera_ficha[0] not in jugador1 or primera_ficha[1] not in jugador1:
                print(f"jugador 1 roba una ficha a no tener ninguna ficha compatible")
                movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                jugador1.append(movimiento)
                movimiento = []
        input(f"Jugador 1 elige una de tus siguientes fichas: {jugador1}")



    # acumulable = ""
    # for i in range(len(doble_mas_alta2)):
    #     acumulable += f"[{doble_mas_alta2[i][0]} : {doble_mas_alta2[i][1]}] "
    # print(f"El acumulable de la jugada es {acumulable}")


domino()