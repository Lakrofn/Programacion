def primosexy(num1):
    essexy = True
    num2 = num1 + 6;
    num3 = num1 - 6;


    for i in range(2, num1):
        if num1 % i == 0:
            essexy = False
    if essexy == True:
        for i in range(2, num2):
            if num2 % i == 0:
                essexy = False
    if essexy == True:
        if num3 > 0:
            for i in range(2, num3):
                if num1 % i == 0:
                    essexy = False
    return essexy
        
print(primosexy(4))