qntd_de_bolas_inicial = int(input())
linha_de_bolas = list(map(int, input().split()))

while qntd_de_bolas_inicial > 1:
    linha_de_bolas_seguintes = []
    for i in range(qntd_de_bolas_inicial - 1):
        if linha_de_bolas[i] == linha_de_bolas[i+1]:
            linha_de_bolas_seguintes.append(1)
        else:
            linha_de_bolas_seguintes.append(-1)
    linha_de_bolas = linha_de_bolas_seguintes
    qntd_de_bolas_inicial -= 1

if linha_de_bolas[0] == 1:
    print("preta")
elif linha_de_bolas[0] == -1:
    print("branca")