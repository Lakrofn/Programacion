def rotar(cadena, rotaciones):
   return (cadena[-rotaciones:] + cadena[:-rotaciones])


print(rotar("alvaro",3))
