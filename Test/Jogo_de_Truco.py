# Função para calcular o valor simbólico de uma carta
def valor_simbolico(carta):
    if carta == 1:
        return 0  # Ás
    elif carta == 2 or carta == 3:
        return 1  # 2 e 3
    elif carta >= 4 and carta <= 7:
        return 2  # 4, 5, 6 e 7
    else:
        return 3  # Q, J, K e A

# Leitura da entrada
N = int(input())

# Inicialização das variáveis
vitorias_tim = 0
vitorias_maia = 0

# Processamento das partidas
if (N%2==0):
    N = N//2
else:
    N = N//2 + 1
for _ in range(N):
    cartas_tim = list(map(int, input().split()))
    cartas_maia = list(map(int, input().split()))

    if all(carta == 0 for carta in cartas_maia):
        vitorias_tim += 1
    else:
        for i in range(3):
            if valor_simbolico(cartas_tim[i]) > valor_simbolico(cartas_maia[i]):
                vitorias_tim += 1
            else:
                vitorias_maia += 1

# Impressão do resultado
print(vitorias_tim, vitorias_maia//2)