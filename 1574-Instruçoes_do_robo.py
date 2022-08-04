qntd_de_sequencias = int(input())
movimentos = []
posicao_robo = []
for i in range(qntd_de_sequencias):
    distancia_percorrida = 0
    n = int(input())
    for j in range(n):
        instrucao = input()
        if instrucao == "LEFT":
            movimentos.append(-1)
        elif instrucao == "RIGHT":
            movimentos.append(1)
        else:
            for b in range(1, n):
                if instrucao == "SAME AS {}".format(b):
                    movimentos.append(movimentos[b - 1])
    for k in movimentos:
        distancia_percorrida += k
    posicao_robo.append(distancia_percorrida)
    movimentos.clear()
for h in posicao_robo:
    print(h)