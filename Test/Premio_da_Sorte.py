# Leitura da entrada
N = int(input())
valores = list(map(int, input().split()))

# Inicialização das variáveis
maior_sequencia = 1
sequencia_atual = 1

# Verificação da maior sequência
for i in range(1, N):
    if valores[i] == valores[i - 1]:
        sequencia_atual += 1
    else:
        maior_sequencia = max(maior_sequencia, sequencia_atual)
        sequencia_atual = 1

# Atualização da maior sequência novamente
maior_sequencia = max(maior_sequencia, sequencia_atual)

# Impressão do resultado
print(maior_sequencia)
