jogos = int(input())
tim = 0
maia = 0
ordem = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]

for i in range(jogos):
    jog1 = 0
    jog2 = 0
    cartas = list(map(int, input().split()))
    for j in range(3):
        ind_um = ordem.index(cartas[j])
        ind_dois = ordem.index(cartas[j+3])
        if ind_um == ind_dois or ind_um > ind_dois:
            jog1 += 1
        else:
            jog2 += 1
    if jog1 > jog2 or jog1 == jog2:
        tim += 1
    else:
        maia += 1

print(f'{tim} {maia}')