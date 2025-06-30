import numpy as np

# Semente para reprodutibilidade dos resultados
seed = 42
np.random.seed(seed)

dados = np.random.rand(10, 3) * 10
print("Dados Originais:\n", dados)

media_colunas = dados.mean(axis=0)
desvio_padrao_colunas = dados.std(axis=0)

print("\nMédia das Colunas:\n", media_colunas)
print("Desvio Padrão das Colunas:\n", desvio_padrao_colunas)

# Normalização utilizando broadcasting
dados_normalizados = (dados - media_colunas) / desvio_padrao_colunas

print("\nDados Normalizados (Média próxima de 0, Desvio Padrão próximo de 1):\n", dados_normalizados)

print("\nMédia dos Dados Normalizados (deve ser próxima de 0):\n", dados_normalizados.mean(axis=0))
print("Desvio Padrão dos Dados Normalizados (deve ser próximo de 1):\n", dados_normalizados.std(axis=0))