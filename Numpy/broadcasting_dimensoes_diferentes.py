import numpy as np

vetor_coluna = np.array([[0], [10], [20], [30], [40]])
vetor_linha = np.array([0, 1, 2])

print("Vetor Coluna (shape {}):\n{}".format(vetor_coluna.shape, vetor_coluna))
print("\nVetor Linha (shape {}):\n{}".format(vetor_linha.shape, vetor_linha))

# Soma com broadcasting
matriz_resultante = vetor_coluna + vetor_linha

print("\nMatriz Resultante (shape {}):\n{}".format(matriz_resultante.shape, matriz_resultante))