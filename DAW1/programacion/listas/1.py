from random import randint

lista = [1,1,3,4,5,8,7,8,7]

# for i in range(10000):
#     lista.append(randint(1000))


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
    actual = 0
    tramo_actual = []
    for i in lista:
        numero = int(i)
        if numero > numero - 1 and numero < numero + 1:
            tramo_actual.append(numero)
            actual += 1
        else:
            if actual > mayor:
                mayor = actual
                tramo_mayor = tramo_actual
            tramo_actual = []
            actual = 0
    return tramo_mayor

print(tramo_mas_largo())

