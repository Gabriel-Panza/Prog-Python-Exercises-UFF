# Bubble Sort
lista = [5, 4, 6, 3, 8, 10, 7, 2, 9, 1]
print(lista)
for i in range(len(lista)):
    for j in range(len(lista) - 1 - i):
        if lista[j]>lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
        print(lista)


print("\n\n")
# Selection Sort
lista = [5, 4, 6, 3, 8, 10, 7, 2, 9, 1]
print(lista)
for i in range(0, len(lista)):
    menor_index = i
    for j in range(menor_index + 1, len(lista)):
        if lista[j]<lista[menor_index]:
            menor_index = j
    # Usa-se a variavel menor_index para fazer somente 1 troca por iteração do segundo loop
    if (i!= menor_index):
        aux = lista[i]
        lista[i] = lista[menor_index]
        lista[menor_index] = aux
    print(lista)