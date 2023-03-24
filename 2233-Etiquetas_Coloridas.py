def ConversionHexa_Decimal(R, G, B):
    R_decimal = 0
    G_decimal = 0
    B_decimal = 0
    
    for i, element in enumerate(R): 
        if element == 'a':
            R_decimal += 10*16**(len(R)-1 - i)                    
        elif element == 'b':
            R_decimal += 11*16**(len(R)-1 - i)
        elif element == 'c':
            R_decimal += 12*16**(len(R)-1 - i)
        elif element == 'd':
            R_decimal += 13*16**(len(R)-1 - i)
        elif element == 'e':
            R_decimal += 14*16**(len(R)-1 - i)
        elif element == 'f':
            R_decimal += 15*16**(len(R)-1 - i)
        else:
            R_decimal += int(element)*16**(len(R)-1 - i)

    for i, element in enumerate(G):
        if element == 'a':
            G_decimal += 10*16**(len(G)-1 - i)                    
        elif element == 'b':
            G_decimal += 11*16**(len(G)-1 - i)
        elif element == 'c':
            G_decimal += 12*16**(len(G)-1 - i)
        elif element == 'd':
            G_decimal += 13*16**(len(G)-1 - i)
        elif element == 'e':
            G_decimal += 14*16**(len(G)-1 - i)
        elif element == 'f':
            G_decimal += 15*16**(len(G)-1 - i)
        else:
            G_decimal += int(element)*16**(len(G)-1 - i)

    for i, element in enumerate(B):
        if element == 'a':
            B_decimal += 10*16**(len(B)-1 - i)            
        elif element == 'b':
            B_decimal += 11*16**(len(B)-1 - i)
        elif element == 'c':
            B_decimal += 12*16**(len(B)-1 - i)
        elif element == 'd':
            B_decimal += 13*16**(len(B)-1 - i)
        elif element == 'e':
            B_decimal += 14*16**(len(B)-1 - i)
        elif element == 'f':
            B_decimal += 15*16**(len(B)-1 - i)
        else:
            B_decimal += int(element)*16**(len(B)-1 - i)

    return(R_decimal, G_decimal, B_decimal)
    

def ConversionDecimal_Hexa(result):
    convert = []
    while result > 0:
        sub = result
        result = result // 16
        rest = int(sub - (result * 16))
        convert.append(rest)

    convert.reverse()

    hexa = str()
    for i in convert:
        if i > 9:
                hexa += str(hexadecimal[i])
        else:
                hexa += str(i)
    return hexa

hexadecimal = [0,0,0,0,0,0,0,0,0,0,'a','b','c','d','e','f']
R = list(input())
G = list(input())
B = list(input())

R_decimal , G_decimal , B_decimal = (ConversionHexa_Decimal(R, G, B))

resultR = 1

if G_decimal > R_decimal:
    print(resultR)
else:
    resultG = (R_decimal//G_decimal)**2
    if B_decimal > G_decimal:
        print(ConversionDecimal_Hexa(resultR+resultG))
    else:
        resultB = ((G_decimal//B_decimal)**2) * resultG
        print(ConversionDecimal_Hexa(resultR+resultG+resultB))