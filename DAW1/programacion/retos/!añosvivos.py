def yearsvivos(nacimiento1, muerte1, nacimiento2, muerte2):
    years = 0
    persona1 =[nacimiento1, muerte1]
    persona2 =[nacimiento2, muerte2]
    if persona1[1] > persona2[0] and persona1[0] < persona2[0]:
        if persona1[1] > persona2[1]:
            years = (persona1[1] - persona2[0]) - (persona1[1] - persona2[1]) + 1
        else:
            years = persona1[1] - persona2[0] + 1
    elif persona2[0] < persona1[0] and persona2[1] > persona1[0]:
        if persona2[1] > persona1[1]:
            years =(persona2[1] - persona1[0]) - (persona2[1] - persona1[1]) + 1
        else:
            years = persona2[1] - persona1[0] + 1
    elif persona1[1] == persona2[0] or persona2[1] == persona1[0]:
        years = 1
    else:
        years = 0

    return years


print(yearsvivos(1900, 1950, 1925, 1940))  # Debería devolver 16
print(yearsvivos(1900, 1950, 1940, 1960))  # Debería devolver 11
print(yearsvivos(1900, 1950, 1951, 1960))  # Debería devolver 0
print(yearsvivos(1900, 1950, 1951, 1951))  # Debería devolver 0
print(yearsvivos(1900, 1950, 1890, 1910))  # Debería devolver 11
print(yearsvivos(1900, 1950, 1880, 1890))  # Debería devolver 0
print(yearsvivos(1900, 1950, 1910, 1920))  # Debería devolver 11
print(yearsvivos(1900, 1950, 2000, 2010))  # Debería devolver 0
print(yearsvivos(1900, 1950, 1800, 1850))  # Debería devolver 0