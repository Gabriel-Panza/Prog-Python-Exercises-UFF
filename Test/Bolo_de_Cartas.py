def calcular_minimo_bolos(n, sequencia):
    diferenca = sequencia[1] - sequencia[0]  # Calcula a diferença entre as duas primeiras cartas
    bolos = 1  # Inicia com um único bolo contendo a primeira carta da sequência

    for i in range(1, n-1):
        if sequencia[i+1] - sequencia[i] != diferenca:
            if i+2<n:
                diferenca = sequencia[i+2] - sequencia[i+1]
                bolos += 1
            else:
                bolos += 1
                break

    return bolos

# Leitura da entrada
n = int(input())  # Número de elementos da sequência
sequencia = list(map(int, input().split()))  # Sequência de números

# Chama a função para calcular o número mínimo de bolos
minimo_bolos = calcular_minimo_bolos(n, sequencia)

# Imprime o resultado
print(minimo_bolos)