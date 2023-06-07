jogadores, rodadas = map(int, input().split())
partidas = [[0,0],[1,0],[2,0]]

for i in range(rodadas):
    partida = []
    for j in range(jogadores):
        numero_sorteado = int(input())
        partida.append(numero_sorteado)
    partidas.append(partida)


maior_pontuacao = 0
index_vencedor = 0
for i in range(jogadores):
    conta_pontos = 0
    for j in range(rodadas):
        conta_pontos += partidas[j][i]
    
    if conta_pontos >= maior_pontuacao:
        maior_pontuacao = conta_pontos
        index_vencedor = i+1
print(index_vencedor)