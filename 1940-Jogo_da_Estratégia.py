Jogadores, Rodadas = [int(x) for x in input().split()]
entrada = list(map(int, input().split()))
pontos = [0] * Jogadores

for i in range(Jogadores):
    pontos[i] = sum(entrada[i::Jogadores])
    
pontos = pontos[::-1]
vencedor = Jogadores - pontos.index(max(pontos))
print(vencedor)