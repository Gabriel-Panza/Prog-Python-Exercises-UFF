N =  int(input())                           # define o numero de registros de raio
vetCoordenadas = []                         # define o vetor de coordenadas
jafoi = [0]*N                               # define o vetor de comparação das coordenadas
contF = 0                                   # define o contador
for i in range(N):
    coordenadas = []
    x,y = map(int,input().split())          # define o valor da coordenada X e Y do quadrante
    coordenadas.append(x)                   # insere as coordenadas x em uma lista
    coordenadas.append(y)                   # insere as coordenadas y em uma lista
    vetCoordenadas.append(coordenadas)      # forma a matriz de coordenadas

    if vetCoordenadas[i] not in jafoi:      # compara coordenadas e adiciona ao vetor, se n forem iguais
        jafoi[i] = vetCoordenadas[i]
    else:                                   # se forem iguais, nao adiciona ao vetor e soma 1 ao contador
        contF+= 1

if contF > 0:                               # se isso for verdade, o raio caiu no mesmo lugar pelo menos uma vez 
    print(1)
else:                                       # se isso for verdade, o raio nunca caiu no mesmo lugar
    print(0)