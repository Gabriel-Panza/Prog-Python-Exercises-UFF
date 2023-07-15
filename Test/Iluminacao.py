def contar_trechos_escuros(n, potencias):
    contagem = 0
    max_contagem = 0

    for i in range(n):
        if potencias[i] + potencias[(i+1)%n] < 1000:
            contagem += 1
            max_contagem = max(max_contagem, contagem)
        else:
            contagem = 0

    return max_contagem

# Leitura da entrada
n = int(input())  # Número de postes
potencias = [int(input()) for _ in range(n)]  # Potências luminosas das lâmpadas

# Chama a função para contar o número máximo de trechos escuros consecutivos
max_trechos_escuros = contar_trechos_escuros(n, potencias)

# Imprime o resultado
print(max_trechos_escuros)