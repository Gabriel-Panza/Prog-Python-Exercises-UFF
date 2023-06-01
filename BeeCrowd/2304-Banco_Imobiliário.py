I, N = map(int, input().split())
D = E = F = I
for i in range(N):
    operacao = input().split()
    valor = int(operacao[len(operacao)-1])
    if operacao[0] == 'C':
        if operacao[1] == 'D':
            D -= valor
        elif operacao[1] == 'E':
            E -= valor
        else:
            F -= valor
    if operacao[0] == 'V':
        if operacao[1] == 'D':
            D += valor
        elif operacao[1] == 'E':
            E += valor
        else:
            F += valor
    if operacao[0] == 'A':
        if operacao[1] == 'D':
            if operacao[2] == 'E':
                D += valor
                E -= valor
            if operacao[2] == 'F':
                D += valor
                F -= valor
        elif operacao[1] == 'E':
            if operacao[2] == 'D':
                E += valor
                D -= valor
            if operacao[2] == 'F':
                E += valor
                F -= valor
        else:
            if operacao[2] == 'E':
                F += valor
                E -= valor
            if operacao[2] == 'D':
                F += valor
                D -= valor
print(D, E, F)