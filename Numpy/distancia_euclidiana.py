import numpy as np

ponto_referencia = np.array([1, 2, 3])
conjunto_pontos = np.random.randint(0, 10, size=(10, 3))

print("Ponto de Referência:\n", ponto_referencia)
print("\nConjunto de Pontos:\n", conjunto_pontos)

# Cálculo da distância euclidiana de forma vetorizada
distancias = np.sqrt(np.sum(np.square(conjunto_pontos - ponto_referencia), axis=1))

print("\nDistância Euclidiana de cada ponto ao ponto de referência:\n", distancias)