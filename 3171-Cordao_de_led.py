# Definimos nossas variáveis que serão usadas no problema
N, L = map(int, input().split())
matriz = [[]] * N
fila = [1]
conectados = [False] * N
avaliador = True

# Preenchemos a matriz com N_segmentos falsos
for i in range(len(matriz)):
    matriz[i] = [False] * N

# Para cada L_linha de conexão tem-se 2 segmentos, 'x' e 'y'
for i in range(L):
    X, Y = map(int, input().split())
    matriz[X - 1][Y - 1] = True
    matriz[Y - 1][X - 1] = True

# Começamos a checar todas as ligações, segmento por segmento.
while len(fila) != 0:
    x = fila.pop(0)
    if not conectados[x]:
        conectados[x] = True
        for i in range(N):
            if matriz[x][i]:
                fila.append(i)

# Pegamos nossa variável avaliadora e analisamos se o vetor está totalmente verdadeiro
for i in conectados:
    avaliador = avaliador and i

# Printamos se é Completo ou Incompleto
if not avaliador:
    print("INCOMPLETO")
else:
    print("COMPLETO")
