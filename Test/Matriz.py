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
for linha in range(3):
    lista = []
    for coluna in range(3):
        elementoInteiro = int(input("Digite um numero: "))
        lista.append(elementoInteiro)
    matriz.append(lista)
print(matriz)

matriz = []
for linha in range(3):
    lista = []
    for coluna in range(3):
        lista.append(int(input("Digite um numero: ")))
    matriz.append(lista)
print(matriz)


print("\n\n")
# Substituindo elementos de uma matriz pre-criada
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(matriz)
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input("Digite um numero diferente de Zero: "))
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
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print(matriz[linha][coluna])
    
for linha in matriz:
    for elemento_coluna in linha:
        print(elemento_coluna)