N = int(input())
partidas = []
rodadas = []
cont = 1
while(N!=0):
    p1 = input()
    p2 = input()
    partida = "Teste " + str(cont)
    rodada = []
    for i in range(N):
        n1,n2 = map(int, input().split())
        if ((n1+n2) % 2 == 0):
            rodada.append(p1)
        else:
            rodada.append(p2)
    rodadas.append(rodada)
    partidas.append(partida)
    N = int(input())
    cont+=1

print("")
for i in range(len(partidas)):
    print(partidas[i])
    for j in range(len(rodadas[i])):
        print(rodadas[i][j])
    print("")
