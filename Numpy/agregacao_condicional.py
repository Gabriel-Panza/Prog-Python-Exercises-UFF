import numpy as np

a = np.arange(10)
print("Array Original 'a':\n", a)

# Criação da condição
condicao_par = (a % 2 == 0)
print("\nCondição (a é par?):\n", condicao_par)

resultado = np.where(condicao_par, a * 2, a - 1)

print("\nResultado final condicionado:\n", resultado)