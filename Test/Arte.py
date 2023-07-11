def verificar_perfil_perfeito(N, alturas):
    for i in range(1, N):
        if alturas[i] + alturas[N - i - 1] != alturas[i - 1] + alturas[N - i]:
            return False
    return True

# Leitura da entrada
N = int(input())
alturas = list(map(int, input().split()))

# Verificação do perfil
perfil_perfeito = verificar_perfil_perfeito(N, alturas)

# Impressão do resultado
if perfil_perfeito:
    print('S')
else:
    print('N')
