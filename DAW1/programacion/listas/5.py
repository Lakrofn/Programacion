import random

def domino(participantes):
    # Estas variables son para repartir las fichas
    fichas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
    jugador1 = []
    jugador2 = []
    jugador3 = []
    jugador4 = []
    movimiento = []
    contador = 0
    # Esta variable es para comprobar si hay fichas restantes que tirar
    fichas_restantes1 = True
    fichas_restantes2 = True
    fichas_restantes3 = True if participantes >= 3 else False
    fichas_restantes4 = True if participantes == 4 else False

    fichas_en_posesion1 = 1
    fichas_en_posesion2 = 1
    fichas_en_posesion3 = 1
    fichas_en_posesion4 = 1
    # Estas variables es para comprobar las fichas que se encuentran en cada extremo
    ultima_ficha = []
    primera_ficha = []
    # Esta variable indica la partida actual
    jugadas =[]
    # Esta variable indica quien va a tirar la siguiente ficha
    turno = 1
    # Estas variables son para sumar los numeros de las fichas restantes de cada jugador en caso de que se queden sin fichas para robar y no sea ninguna valida
    empate = True
    suma_fichas1 = 0
    suma_fichas2 = 0
    suma_fichas3 = 0
    suma_fichas4 = 0
    # Esta variable es para almacenar la eleccion del jugador
    lista_eleccion = []
    # Esta variable es para comprobar si hay fichas restantes que tirar


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

    while contador < 7 and participantes >= 3:
        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
        jugador3.append(movimiento)
        movimiento = []
        contador += 1
    contador = 0

    while contador < 7 and participantes == 4:
        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
        jugador4.append(movimiento)
        movimiento = []
        contador += 1
    contador = 0
    
    doble_mas_alta1 = []
    doble_mas_alta2 = []
    doble_mas_alta3 = []
    doble_mas_alta4 = []
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
    for i in jugador3:
        if i[0] == i[1]:
            doble_actual.append(i)
            if doble_actual > doble_mas_alta3:
                doble_mas_alta3 = doble_actual
        doble_actual = []
    for i in jugador4:
        if i[0] == i[1]:
            doble_actual.append(i)
            if doble_actual > doble_mas_alta4:
                doble_mas_alta4 = doble_actual
        doble_actual = []

    if doble_mas_alta1 > doble_mas_alta2 and doble_mas_alta1 > doble_mas_alta3 and doble_mas_alta1 > doble_mas_alta4:
        print(f"El jugador 1 empieza con {doble_mas_alta1[0]}")
        jugadas.append(doble_mas_alta1[0])
        jugador1.remove(doble_mas_alta1[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta1[0]
        primera_ficha = doble_mas_alta1[0]
        turno = 1

    elif doble_mas_alta2 > doble_mas_alta1 and doble_mas_alta2 > doble_mas_alta3 and doble_mas_alta2 > doble_mas_alta4:
        print(f"El jugador 2 empieza con {doble_mas_alta2[0]}")
        jugadas.append(doble_mas_alta2[0])
        jugador2.remove(doble_mas_alta2[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta2[0]
        primera_ficha = doble_mas_alta2[0]
        turno = 2

    elif doble_mas_alta3 > doble_mas_alta1 and doble_mas_alta3 > doble_mas_alta2 and doble_mas_alta3 > doble_mas_alta4:
        print(f"El jugador 2 empieza con {doble_mas_alta3[0]}")
        jugadas.append(doble_mas_alta3[0])
        jugador3.remove(doble_mas_alta3[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta3[0]
        primera_ficha = doble_mas_alta3[0]
        turno = 3

    elif doble_mas_alta4 > doble_mas_alta1 and doble_mas_alta4 > doble_mas_alta2 and doble_mas_alta4 > doble_mas_alta3:
        print(f"El jugador 2 empieza con {doble_mas_alta4[0]}")
        jugadas.append(doble_mas_alta4[0])
        jugador4.remove(doble_mas_alta4[0])
        print(f"La jugada actual es {jugadas}")
        ultima_ficha = doble_mas_alta4[0]
        primera_ficha = doble_mas_alta4[0]
        turno = 4

    # Compruebo si siguen habiendo fichas para tirar
    while fichas_restantes1 == True or fichas_restantes2 == True or fichas_restantes3 == True or fichas_restantes4 == True:
        if fichas_en_posesion1 == 1 and fichas_en_posesion2 == 1 and fichas_en_posesion3 == 1 and fichas_en_posesion4 == 1:

            # Compruebo si le toca al jugador 1
            if turno == 1:
                # Compruebo si el jugador tiene mas fichas para jugar
                if jugador1 != []:
                    # comprobamos si el jugador 1 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    fichas_posibles = []
                    for extremo in range(len(primera_ficha)):
                        if extremo == 0:
                            for fichas_jugador in range(len(jugador1)):
                                for valida in jugador1[fichas_jugador]:
                                    if valida == primera_ficha[extremo]:
                                        fichas_posibles.append(jugador1[fichas_jugador]) if jugador1[fichas_jugador] not in fichas_posibles else None
                    for extremo in range(len(ultima_ficha)):
                        if extremo == 1:
                            for fichas_jugador in range(len(jugador1)):
                                for valida in jugador1[fichas_jugador]:
                                    if valida == ultima_ficha[extremo]:
                                        fichas_posibles.append(jugador1[fichas_jugador]) if jugador1[fichas_jugador] not in fichas_posibles else None

                    # Si no tiene ficha valida, roba hasta que tenga una o se queden sin fichas
                    while len(fichas_posibles) == 0 and len(fichas) != 0:
                        print("Jugador 1 tiene que robar una ficha")
                        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                        jugador1.append(movimiento)
                        fichas_posibles.append(movimiento) if movimiento[0] == jugadas[0][0] or movimiento[1] == jugadas[0][0] or movimiento[0] == jugadas[-1][1] or movimiento[1] == jugadas[-1][1] else None
                        movimiento = []

                    # comprobamos si el jugador 1 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    if len(fichas_posibles) != 0:
                        fichas_restantes1 = True
                        eleccion = input(f"Jugador 1 elige una de tus siguientes fichas: {jugador1} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                        eleccion_num1 = 0
                        eleccion_num2 = 0
                        for i in range(len(eleccion)):
                            if eleccion[i].isdigit():
                                if i == 0:
                                    eleccion_num1 = int(eleccion[i])
                                else:
                                    eleccion_num2 = int(eleccion[i])
                        for x in range(len(jugador1)):
                            if eleccion_num1 == jugador1[x][0] and eleccion_num2 == jugador1[x][1]:
                                lista_eleccion = jugador1[x]
                        
                        # comprobamos que la ficha elegida es valida y si no lo es le pedimos otra
                        while lista_eleccion not in fichas_posibles and len(fichas_posibles) != 0:
                            eleccion = input(f"Esa ficha no es valida, elige otra ficha, tus fichas validas son: {fichas_posibles} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                            eleccion_num1 = 0
                            eleccion_num2 = 0
                            for i in range(len(eleccion)):
                                if eleccion[i].isdigit():
                                    if i == 0:
                                        eleccion_num1 = int(eleccion[i])
                                    else:
                                        eleccion_num2 = int(eleccion[i])
                            for x in range(len(jugador1)):
                                if eleccion_num1 == jugador1[x][0] and eleccion_num2 == jugador1[x][1]:
                                    lista_eleccion = jugador1[x]
                        
                        # Comprobamos en que posicion se puede colocar la ficha
                        if lista_eleccion[0] == jugadas[0][0] or lista_eleccion[1] == jugadas[0][0]:
                            # Si el numero que encaja es el primer numero de la ficha elegida se da la vuelta y se coloca en la primera posicion
                            if lista_eleccion[0] == jugadas[0][0]:
                                jugadas.insert(0, lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador1.remove(lista_eleccion)
                                print(f"El jugador 1 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 2
                            else:
                                # Si el numero que encaja es el segundo numero de la ficha elegida se coloca en la primera posicion
                                jugadas.insert(0, lista_eleccion)
                                fichas_posibles = []
                                jugador1.remove(lista_eleccion)
                                print(f"El jugador 1 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 2
                        elif lista_eleccion[0] == jugadas[-1][1] or lista_eleccion[1] == jugadas[-1][1]:
                            # Si el numero que encaja es el primer numero de la ficha elegida se da la vuelta y se coloca en la ultima posicion
                            if lista_eleccion[1] == jugadas[-1][1]:
                                jugadas.append(lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador1.remove(lista_eleccion)
                                print(f"El jugador 1 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 2
                            else:
                                # Si el numero que encaja es el segundo numero de la ficha elegida se coloca en la ultima posicion
                                jugadas.append(lista_eleccion)
                                fichas_posibles = []
                                jugador1.remove(lista_eleccion)
                                print(f"El jugador 1 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 2
                    else:
                        print("Jugador 1 no tiene fichas validas y no quedan fichas para robar, pasa turno")
                        turno = 2
                        fichas_restantes1 = False
                else:
                    fichas_en_posesion1 = 0
            
            # Compruebo si le toca al jugador 2
            elif turno == 2:
                # Compruebo si el jugador tiene mas fichas para jugar
                if jugador2 != []:
                    # comprobamos si el jugador 2 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    fichas_posibles = []
                    for extremo in range(len(primera_ficha)):
                        if extremo == 0:
                            for fichas_jugador in range(len(jugador2)):
                                for valida in jugador2[fichas_jugador]:
                                    if valida == primera_ficha[extremo]:
                                        fichas_posibles.append(jugador2[fichas_jugador]) if jugador2[fichas_jugador] not in fichas_posibles else None
                    for extremo in range(len(ultima_ficha)):
                        if extremo == 1:
                                for fichas_jugador in range(len(jugador2)):
                                    for valida in jugador2[fichas_jugador]:
                                        if valida == ultima_ficha[extremo]:
                                            fichas_posibles.append(jugador2[fichas_jugador]) if jugador2[fichas_jugador] not in fichas_posibles else None
                    # Si no tiene ficha valida, roba hasta que tenga una o se queden sin fichas
                    while len(fichas_posibles) == 0 and len(fichas) != 0:
                        print("Jugador 2 tiene que robar una ficha")
                        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                        jugador2.append(movimiento)
                        fichas_posibles.append(movimiento) if movimiento[0] == jugadas[0][0] or movimiento[1] == jugadas[0][0] or movimiento[0] == jugadas[-1][1] or movimiento[1] == jugadas[-1][1] else None
                        movimiento = []
                    # Si tiene, le pedimos que elija una ficha
                    if len(fichas_posibles) != 0:
                        fichas_restantes2 = True
                        eleccion = input(f"Jugador 2 elige una de tus siguientes fichas: {jugador2} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                        eleccion_num1 = 0
                        eleccion_num2 = 0
                        for i in range(len(eleccion)):
                            if eleccion[i].isdigit():
                                if i == 0:
                                    eleccion_num1 = int(eleccion[i])
                                else:
                                    eleccion_num2 = int(eleccion[i])
                        for x in range(len(jugador2)):
                            if eleccion_num1 == jugador2[x][0] and eleccion_num2 == jugador2[x][1]:
                                lista_eleccion = jugador2[x]

                        # comprobamos que la ficha elegida es valida y si no lo es le pedimos otra
                        while lista_eleccion not in fichas_posibles and len(fichas_posibles) != 0:
                            eleccion = input(f"Esa ficha no es valida, elige otra ficha, tus fichas validas son: {fichas_posibles} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                            eleccion_num1 = 0
                            eleccion_num2 = 0
                            for i in range(len(eleccion)):
                                if eleccion[i].isdigit():
                                    if i == 0:
                                        eleccion_num1 = int(eleccion[i])
                                    else:
                                        eleccion_num2 = int(eleccion[i])
                            for x in range(len(jugador2)):
                                if eleccion_num1 == jugador2[x][0] and eleccion_num2 == jugador2[x][1]:
                                    lista_eleccion = jugador2[x]
                        # Comprobamos en que posicion se puede colocar la ficha
                        if lista_eleccion[0] == jugadas[0][0] or lista_eleccion[1] == jugadas[0][0]:
                            # Si el numero que encaja es el primer numero de la ficha elegida se da la vuelta y se coloca en la primera posicion
                            if lista_eleccion[0] == jugadas[0][0]:
                                jugadas.insert(0, lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador2.remove(lista_eleccion)
                                print(f"El jugador 2 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 3 if participantes == 3 else 1
                            else:
                                # Si el numero que encaja es el segundo numero de la ficha elegida se coloca en la primera posicion
                                jugadas.insert(0, lista_eleccion)
                                fichas_posibles = []
                                jugador2.remove(lista_eleccion)
                                print(f"El jugador 2 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 3 if participantes == 3 else 1
                        elif lista_eleccion[0] == jugadas[-1][1] or lista_eleccion[1] == jugadas[-1][1]:
                            # Si el numero que encaja es el segundo numero de la ficha elegida se da la vuelta y se coloca en la ultima posicion
                            if lista_eleccion[1] == jugadas[-1][1]:
                                jugadas.append(lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador2.remove(lista_eleccion)
                                print(f"El jugador 2 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 3 if participantes == 3 else 1
                            else:
                                # Si el numero que encaja es el primer numero de la ficha elegida se coloca en la ultima posicion
                                jugadas.append(lista_eleccion)
                                fichas_posibles = []
                                jugador2.remove(lista_eleccion)
                                print(f"El jugador 2 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 3 if participantes == 3 else 1
                    else:
                        print("Jugador 2 no tiene fichas validas y no quedan fichas para robar, pasa turno")
                        turno = 3 if participantes == 3 else 1
                        fichas_restantes2 = False
                else:
                    fichas_en_posesion2 = 0


            # Compruebo si le toca al jugador 3
            elif turno == 3:
                # Compruebo si el jugador tiene mas fichas para jugar
                if jugador3 != []:
                    # comprobamos si el jugador 3 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    fichas_posibles = []
                    for extremo in range(len(primera_ficha)):
                        if extremo == 0:
                            for fichas_jugador in range(len(jugador3)):
                                for valida in jugador3[fichas_jugador]:
                                    if valida == primera_ficha[extremo]:
                                        fichas_posibles.append(jugador3[fichas_jugador]) if jugador3[fichas_jugador] not in fichas_posibles else None
                    for extremo in range(len(ultima_ficha)):
                        if extremo == 1:
                            for fichas_jugador in range(len(jugador3)):
                                for valida in jugador3[fichas_jugador]:
                                    if valida == ultima_ficha[extremo]:
                                        fichas_posibles.append(jugador3[fichas_jugador]) if jugador3[fichas_jugador] not in fichas_posibles else None

                    # Si no tiene ficha valida, roba hasta que tenga una o se queden sin fichas
                    while len(fichas_posibles) == 0 and len(fichas) != 0:
                        print("Jugador 3 tiene que robar una ficha")
                        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                        jugador3.append(movimiento)
                        fichas_posibles.append(movimiento) if movimiento[0] == jugadas[0][0] or movimiento[1] == jugadas[0][0] or movimiento[0] == jugadas[-1][1] or movimiento[1] == jugadas[-1][1] else None
                        movimiento = []

                    # comprobamos si el jugador 3 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    if len(fichas_posibles) != 0:
                        fichas_restantes3 = True
                        eleccion = input(f"Jugador 3 elige una de tus siguientes fichas: {jugador3} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                        eleccion_num1 = 0
                        eleccion_num2 = 0
                        for i in range(len(eleccion)):
                            if eleccion[i].isdigit():
                                if i == 0:
                                    eleccion_num1 = int(eleccion[i])
                                else:
                                    eleccion_num2 = int(eleccion[i])
                        for x in range(len(jugador3)):
                            if eleccion_num1 == jugador3[x][0] and eleccion_num2 == jugador3[x][1]:
                                lista_eleccion = jugador3[x]

                        # comprobamos que la ficha elegida es valida y si no lo es le pedimos otra
                        while lista_eleccion not in fichas_posibles and len(fichas_posibles) != 0:
                            eleccion = input(f"Esa ficha no es valida, elige otra ficha, tus fichas validas son: {fichas_posibles} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                            eleccion_num1 = 0
                            eleccion_num2 = 0
                            for i in range(len(eleccion)):
                                if eleccion[i].isdigit():
                                    if i == 0:
                                        eleccion_num1 = int(eleccion[i])
                                    else:
                                        eleccion_num2 = int(eleccion[i])
                            for x in range(len(jugador3)):
                                if eleccion_num1 == jugador3[x][0] and eleccion_num2 == jugador3[x][1]:
                                    lista_eleccion = jugador3[x]
                        # Comprobamos en que posicion se puede colocar la ficha
                        if lista_eleccion[0] == jugadas[0][0] or lista_eleccion[1] == jugadas[0][0]:
                            # Si el numero que encaja es el primer numero de la ficha elegida se da la vuelta y se coloca en la primera posicion
                            if lista_eleccion[0] == jugadas[0][0]:
                                jugadas.insert(0, lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador3.remove(lista_eleccion)
                                print(f"El jugador 3 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 1
                            else:
                                # Si el numero que encaja es el segundo numero de la ficha elegida se coloca en la primera posicion
                                jugadas.insert(0, lista_eleccion)
                                fichas_posibles = []
                                jugador3.remove(lista_eleccion)
                                print(f"El jugador 3 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 1
                        elif lista_eleccion[0] == jugadas[-1][1] or lista_eleccion[1] == jugadas[-1][1]:
                            # Si el numero que encaja es el segundo numero de la ficha elegida se da la vuelta y se coloca en la ultima posicion
                            if lista_eleccion[1] == jugadas[-1][1]:
                                jugadas.append(lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador3.remove(lista_eleccion)
                                print(f"El jugador 3 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 1
                            else:
                                # Si el numero que encaja es el primer numero de la ficha elegida se coloca en la ultima posicion
                                jugadas.append(lista_eleccion)
                                fichas_posibles = []
                                jugador3.remove(lista_eleccion)
                                print(f"El jugador 3 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 1
                    else:
                        print("Jugador 3 no tiene fichas validas y no quedan fichas para robar, pasa turno")
                        fichas_restantes3 = False
                        turno = 1
                else:
                    fichas_en_posesion3 = 0


            # Compruebo si le toca al jugador 4
            elif turno == 4:
                # Compruebo si el jugador tiene mas fichas para jugar
                if jugador4 != []:
                    # comprobamos si el jugador 4 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    fichas_posibles = []
                    for extremo in range(len(primera_ficha)):
                        if extremo == 0:
                            for fichas_jugador in range(len(jugador4)):
                                for valida in jugador4[fichas_jugador]:
                                    if valida == primera_ficha[extremo]:
                                        fichas_posibles.append(jugador4[fichas_jugador]) if jugador4[fichas_jugador] not in fichas_posibles else None
                    for extremo in range(len(ultima_ficha)):
                        if extremo == 1:
                            for fichas_jugador in range(len(jugador4)):
                                for valida in jugador4[fichas_jugador]:
                                    if valida == ultima_ficha[extremo]:
                                        fichas_posibles.append(jugador4[fichas_jugador]) if jugador4[fichas_jugador] not in fichas_posibles else None
                    
                    # Si no tiene ficha valida, roba hasta que tenga una o se queden sin fichas
                    while len(fichas_posibles) == 0 and len(fichas) != 0:
                        print("Jugador 4 tiene que robar una ficha")
                        movimiento = fichas.pop(random.randint(0, len(fichas)-1))
                        jugador4.append(movimiento)
                        fichas_posibles.append(movimiento) if movimiento[0] == jugadas[0][0] or movimiento[1] == jugadas[0][0] or movimiento[0] == jugadas[-1][1] or movimiento[1] == jugadas[-1][1] else None
                        movimiento = []
                    
                    # comprobamos si el jugador 4 tiene una ficha en la primera o ultima posicion y sino robara hasta que tenga una en caso de que no tenga aun asi pasara
                    if len(fichas_posibles) != 0:
                        fichas_restantes4 = True
                        eleccion = input(f"Jugador 4 elige una de tus siguientes fichas: {jugador4} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                        eleccion_num1 = 0
                        eleccion_num2 = 0
                        for i in range(len(eleccion)):
                            if eleccion[i].isdigit():
                                if i == 0:
                                    eleccion_num1 = int(eleccion[i])
                                else:
                                    eleccion_num2 = int(eleccion[i])
                        for x in range(len(jugador3)):
                            if eleccion_num1 == jugador4[x][0] and eleccion_num2 == jugador4[x][1]:
                                lista_eleccion = jugador4[x]

                        # comprobamos que la ficha elegida es valida y si no lo es le pedimos otra
                        while lista_eleccion not in fichas_posibles and len(fichas_posibles) != 0:    
                            eleccion = input(f"Esa ficha no es valida, elige otra ficha, tus fichas validas son: {fichas_posibles} (Escribe solamente los numeros sin los corchetes ej: 5,5): ")
                            eleccion_num1 = 0
                            eleccion_num2 = 0
                            for i in range(len(eleccion)):
                                if eleccion[i].isdigit():
                                    if i == 0:
                                        eleccion_num1 = int(eleccion[i])
                                    else:
                                        eleccion_num2 = int(eleccion[i])
                            for x in range(len(jugador4)):
                                if eleccion_num1 == jugador4[x][0] and eleccion_num2 == jugador4[x][1]:
                                    lista_eleccion = jugador4[x]
                        # Comprobamos en que posicion se puede colocar la ficha
                        if lista_eleccion[0] == jugadas[0][0] or lista_eleccion[1] == jugadas[0][0]:
                            # Si el numero que encaja es el primer numero de la ficha elegida se da la vuelta y se coloca en la primera posicion
                            if lista_eleccion[0] == jugadas[0][0]:
                                jugadas.insert(0, lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador4.remove(lista_eleccion)
                                print(f"El jugador 4 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                primera_ficha = jugadas[0]
                                turno = 1
                            else:
                                # Si el numero que encaja es el segundo numero de la ficha elegida se coloca en la primera posicion
                                jugadas.insert(0, lista_eleccion)
                                fichas_posibles = []
                                jugador4.remove(lista_eleccion)
                                print(f"El jugador 4 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}") 
                                primera_ficha = jugadas[0]
                                turno = 1
                        elif lista_eleccion[0] == jugadas[-1][1] or lista_eleccion[1] == jugadas[-1][1]:
                            # Si el numero que encaja es el segundo numero de la ficha elegida se da la vuelta y se coloca en la ultima posicion
                            if lista_eleccion[1] == jugadas[-1][1]:
                                jugadas.append(lista_eleccion[::-1])
                                fichas_posibles = []
                                jugador4.remove(lista_eleccion)
                                print(f"El jugador 4 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 1
                            else:
                                # Si el numero que encaja es el primer numero de la ficha elegida se coloca en la ultima posicion
                                jugadas.append(lista_eleccion)
                                fichas_posibles = []
                                jugador4.remove(lista_eleccion)
                                print(f"El jugador 4 usa la ficha {lista_eleccion}")
                                print(f"La jugada actual es {jugadas}")
                                ultima_ficha = jugadas[-1]
                                turno = 1
                    else:
                        print("Jugador 4 no tiene fichas validas y no quedan fichas para robar, pasa turno")
                        turno = 1
                        fichas_restantes4 = False  
                else:
                    fichas_en_posesion4 = 0

        # Compruebo quien ha sido el ganador de la partida
        else:
            if jugador1 == []:
                print("Jugador 1 ha ganado la partida")
                empate = False
                fichas_restantes1 = False
                fichas_restantes2 = False
                fichas_restantes3 = False
                fichas_restantes4 = False
            elif jugador2 == []:
                print("Jugador 2 ha ganado la partida")
                empate = False
                fichas_restantes1 = False
                fichas_restantes2 = False
                fichas_restantes3 = False
                fichas_restantes4 = False
            elif jugador3 == [] and participantes == 3:
                print("Jugador 3 ha ganado la partida")
                empate = False
                fichas_restantes1 = False
                fichas_restantes2 = False
                fichas_restantes3 = False
                fichas_restantes4 = False
            elif jugador4 == [] and participantes == 4:
                print("Jugador 4 ha ganado la partida")
                empate = False
                fichas_restantes1 = False
                fichas_restantes2 = False
                fichas_restantes3 = False
                fichas_restantes4 = False

    if empate == True:
        # Comprobamos quien ha ganado
        if len(jugador1) == 0:
            print("El jugador 1 ha ganado")
        elif len(jugador2) == 0:
            print("El jugador 2 ha ganado")
        elif len(jugador3) == 0 and participantes == 3:
            print("El jugador 3 ha ganado")
        elif len(jugador4) == 0 and participantes == 4:
            print("El jugador 4 ha ganado")
        # Si ambos jugadores se quedan sin fichas validas y sin fichas para robar, se suman las fichas restantes de cada jugador y gana el que tenga menos
        else:
            for numero1 in jugador1:
                for suma1 in numero1:
                    suma_fichas1 += suma1
            for numero2 in jugador2:
                for suma2 in numero2:
                    suma_fichas2 += suma2
            for numero3 in jugador3: 
                for suma3 in numero3:
                    suma_fichas3 += suma3
            for numero4 in jugador4:
                for suma4 in numero4:
                    suma_fichas4 += suma4

            # El que sumado todos los numeros de las fichas restantes tenga menos gana
            if suma_fichas1 < suma_fichas2 and suma_fichas1 < suma_fichas3 and suma_fichas1 < suma_fichas4:
                print("El jugador 1 ha ganado ya que la suma de las fichas restantes es menor")
            elif suma_fichas1 > suma_fichas2 and suma_fichas1 > suma_fichas3 and suma_fichas1 > suma_fichas4:
                print("El jugador 2 ha ganado ya que la suma de las fichas restantes es menor")
            elif suma_fichas3 < suma_fichas2 and suma_fichas3 < suma_fichas1 and suma_fichas3 < suma_fichas4 and participantes >= 3:
                print("El jugador 3 ha ganado ya que la suma de las fichas restantes es menor")
            elif suma_fichas4 < suma_fichas2 and suma_fichas4 < suma_fichas1 and suma_fichas4 < suma_fichas3 and participantes == 4:
                print("El jugador 4 ha ganado ya que la suma de las fichas restantes es menor")
            else:
                print("Empate ya que la suma de las fichas restantes es igual")



domino(3)