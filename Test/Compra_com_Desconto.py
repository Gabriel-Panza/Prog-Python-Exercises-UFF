def calcular_menor_preco(N, precos):
    precos.sort(reverse=True)
    total = 0
    grupos = N // 3

    for i in range(grupos):
        total += (precos[3 * i] + precos[3 * i + 1])

    restantes = N % 3
    if restantes == 1:
        total += precos[-1]
    elif restantes == 2:
        total += (precos[-1] + precos[-2])

    return total

# Leitura da entrada
N = int(input())
precos = []

for _ in range(N):
    preco = int(input())
    precos.append(preco)

# Cálculo do menor preço a pagar
menor_preco = calcular_menor_preco(N, precos)

# Impressão do resultado
print(menor_preco)
