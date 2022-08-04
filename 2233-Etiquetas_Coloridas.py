def ConversaoHexa_Decimal(R, G, B):
    R_decimal = 0
    G_decimal = 0
    B_decimal = 0
    
    for i, elemento in enumerate(R): 
        if elemento == 'a':
            R_decimal += 10*16**(len(R)-1 - i)                    
        elif elemento == 'b':
            R_decimal += 11*16**(len(R)-1 - i)
        elif elemento == 'c':
            R_decimal += 12*16**(len(R)-1 - i)
        elif elemento == 'd':
            R_decimal += 13*16**(len(R)-1 - i)
        elif elemento == 'e':
            R_decimal += 14*16**(len(R)-1 - i)
        elif elemento == 'f':
            R_decimal += 15*16**(len(R)-1 - i)
        else:
            R_decimal += int(elemento)*16**(len(R)-1 - i)

    for i, elemento in enumerate(G):
        if elemento == 'a':
            G_decimal += 10*16**(len(G)-1 - i)                    
        elif elemento == 'b':
            G_decimal += 11*16**(len(G)-1 - i)
        elif elemento == 'c':
            G_decimal += 12*16**(len(G)-1 - i)
        elif elemento == 'd':
            G_decimal += 13*16**(len(G)-1 - i)
        elif elemento == 'e':
            G_decimal += 14*16**(len(G)-1 - i)
        elif elemento == 'f':
            G_decimal += 15*16**(len(G)-1 - i)
        else:
            G_decimal += int(elemento)*16**(len(G)-1 - i)

    for i, elemento in enumerate(B):
        if elemento == 'a':
            B_decimal += 10*16**(len(B)-1 - i)            
        elif elemento == 'b':
            B_decimal += 11*16**(len(B)-1 - i)
        elif elemento == 'c':
            B_decimal += 12*16**(len(B)-1 - i)
        elif elemento == 'd':
            B_decimal += 13*16**(len(B)-1 - i)
        elif elemento == 'e':
            B_decimal += 14*16**(len(B)-1 - i)
        elif elemento == 'f':
            B_decimal += 15*16**(len(B)-1 - i)
        else:
            B_decimal += int(elemento)*16**(len(B)-1 - i)

    return(R_decimal, G_decimal, B_decimal)
    

def ConversaoDecimal_Hexa(resultado):
    convertido = []
    while resultado > 0:
        sub = resultado
        resultado = resultado // 16
        restinho = int(sub - (resultado * 16))
        convertido.append(restinho)

    convertido.reverse()

    hexa = str()
    for i in convertido:
        if i > 9:
                hexa += str(hexadecimal[i])
        else:
                hexa += str(i)
    return hexa

hexadecimal = [0,0,0,0,0,0,0,0,0,0,'a','b','c','d','e','f']
R = list(input())
G = list(input())
B = list(input())

R_decimal , G_decimal , B_decimal = (ConversaoHexa_Decimal(R, G, B))

resultadoR = 1

if G_decimal > R_decimal:
    print(resultadoR)
else:
    resultadoG = (R_decimal//G_decimal)**2
    if B_decimal > G_decimal:
        print(ConversaoDecimal_Hexa(resultadoR+resultadoG))
    else:
        resultadoB = ((G_decimal//B_decimal)**2) * (resultadoG)
        print(ConversaoDecimal_Hexa(resultadoR+resultadoG+resultadoB))