# Definindo nossas variaveis
N_pinos, altura_M = map(int, input().split())
movimentos = 0
altura_dos_pinos = list(map(int, input().split()))

# Indo do primeiro ao ultimo
for i in range(len(altura_dos_pinos)):
    while altura_dos_pinos[i] != altura_M:
        if altura_dos_pinos[i] < altura_M:
            altura_dos_pinos[i] += 1
            altura_dos_pinos[i + 1] += 1
            movimentos += 1

        elif altura_dos_pinos[i] > altura_M:
            altura_dos_pinos[i] -= 1
            altura_dos_pinos[i + 1] -= 1
            movimentos += 1

# Checando se o ultimo número está igual a altura limite que nem seus antecessores
while altura_dos_pinos[-1] != altura_M:
    if altura_dos_pinos[-1] < altura_M:
        altura_dos_pinos[-1] += 1
        movimentos += 1

    elif altura_dos_pinos[-1] > altura_M:
        altura_dos_pinos[-1] -= 1
        movimentos += 1

# Printando os movimentos
print(movimentos)
