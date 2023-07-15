def equilibrar_peso_estudantes(n, pesos):
    soma_pesos = sum(pesos)
    peso_equilibrado = soma_pesos // n  # Calcula o peso que cada estudante deve carregar
    diferenca = [peso - peso_equilibrado for peso in pesos]  # Calcula a diferença de peso para cada estudante

    return diferenca

# Leitura da entrada
n = int(input())  # Número de estudantes
pesos = [int(input()) for _ in range(n)]  # Pesos carregados por cada estudante

# Chama a função para equilibrar o peso entre os estudantes
diferenca_peso = equilibrar_peso_estudantes(n, pesos)

# Imprime a diferença de peso para cada estudante
for diferenca in diferenca_peso:
    print(diferenca*(-1))