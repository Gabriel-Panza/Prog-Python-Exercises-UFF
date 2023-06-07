# Criando uma matriz
matriz1 = [[]]
print(matriz1)
matriz2 = [[]*3]*10
print(matriz2)
matriz3 = [[0]]
print(matriz3)
matriz4 = [[0]*3]*10
print(matriz4)


print("\n\n")
# Adicionando elementos em uma matriz vazia
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elementoInteiro = int(input("Digite um numero: "))
        linha.append(elementoInteiro)
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input("Digite um numero: ")))
    matriz.append(linha)
print(matriz)


print("\n\n")
# Substituindo elementos de uma matriz pre-criada
matriz = [[3, 3, 3], [2, 2, 2], [3, 3, 3]]
print(matriz)
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite um numero diferente de Zero: "))
print(matriz)

matriz[1][1] = int(input("Digite outro numero: "))
print(matriz)


print("\n\n")
# Removendo elementos
matriz = [[1, 2, 3], [4, "Pedro", 6], ["Gabriel", 8], [9,10]]
matriz[2].remove("Gabriel")
matriz[1].remove("Pedro")
print(matriz)

matriz = [[1, 2, 3], [4, "Pedro", 6], ["Gabriel", 8], [9,10]]
matriz[1].pop(1)
matriz[2].pop(0)
print(matriz)

matriz = [[1, 2, 3], [4, "Pedro", 6], ["Gabriel", 8], [9,10]]
matriz.pop(3)
print(matriz)

matriz.clear()
print(matriz)


print("\n\n")
# Percorrendo uma matriz
matriz = [[1, 2, 3], [4, "Pedro", 6], ["Gabriel", 8], [9,10]]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])
print()
for i in matriz:
    for elemento_coluna in i:
        print(elemento_coluna)