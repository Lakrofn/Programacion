from random import randint

lista = []

for i in range(10001):
    lista.append(randint(1, 1001))


# A
def mayor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

# B
def menor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

# C
def suma():
    suma = 0
    for i in lista:
        suma += int(i)
    return suma

# D
def media():
    media = 0
    for i in lista:
        media += int(i)
    return media / len(lista)

# E
def sustituir(lista, valor, reemplazo):
    for i in range(len(lista)):
        if lista[i] == valor:
            lista[i] = reemplazo
    return lista
    

# F
def borrar(lista, valor):
    while valor in lista:
        lista.remove(valor)
    return lista
    
# G
def mostrar():
    return lista

# H
def tramo_mas_largo():
    mayor = 0
    tramo_mayor = []
    posicion_mayor = []
    actual = 0
    tramo_actual = [lista[0]]
    posicion_actual = [0]
    numero_anterior = lista[0]
    for i in range(len(lista)):
        if i != 0 and (lista[i] - 1) == numero_anterior:
            tramo_actual.append(lista[i])
            posicion_actual.append(i)
            numero_anterior = lista[i]
            actual += 1
        elif actual > mayor:
            mayor = actual
            tramo_mayor = tramo_actual
            posicion_mayor = posicion_actual
        else:
            actual = 0
            tramo_actual = [lista[i]]
            posicion_actual = [i]
            numero_anterior = lista[i]
    return print(f"El mayor tramo es {tramo_mayor} que estan en la posicion {posicion_mayor}")

tramo_mas_largo()
#print(mostrar())