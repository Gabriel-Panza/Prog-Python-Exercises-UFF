participantes, rodadas = map(int, input().split())
cont=1 
while participantes!=0 or rodadas != 0:
    fila_inicial = list(map(int, input().split()))
    for i in range(rodadas):
        rodada = list(map(int, input().split()))
        participantesRestantes = rodada[2:]
        while 0 in fila_inicial:
            fila_inicial.remove(0)
        for j in range(len(participantesRestantes)):
            if participantesRestantes[j] != rodada[1]:
                fila_inicial[j] = 0           
    vencedor = max(fila_inicial)
    print("Teste {}".format(cont))
    print(vencedor)
    print()
    cont+=1
    participantes, rodadas = map(int, input().split())