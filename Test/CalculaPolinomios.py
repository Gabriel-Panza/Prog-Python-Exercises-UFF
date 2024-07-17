import numpy as np

# Definindo as equações
A = np.array([
    [0**3, 0**2, 0, 1],
    [1**3, 1**2, 1, 1],
    [2**3, 2**2, 2, 1],
    [3**3, 3**2, 3, 1],
    [4**3, 4**2, 4, 1],
    [5**3, 5**2, 5, 1],
    [6**3, 6**2, 6, 1],
    [7**3, 7**2, 7, 1],
    [8**3, 8**2, 8, 1],
    [9**3, 9**2, 9, 1],
    [10**3, 10**2, 10, 1]
])

# Definindo o resultado das equações
B = np.array([5, 26, 67, 146, 281, 490, 791, 1202, 1741, 2426, 3275])

# Resolvendo o sistema linear de equações
coefficients = np.linalg.lstsq(A, B, rcond=None)[0]
print(coefficients)
