N_elem = int(input())
elem_sequencia = list(map(int, input().split()))
blocos = []
lista_de_blocos = []
razao = elem_sequencia[1] - elem_sequencia[0]
blocos.append(elem_sequencia[0])
for i in range (1,N_elem-1):
    if (elem_sequencia[i] - elem_sequencia[i-1]) == razao:
        blocos.append(elem_sequencia[i])
    else:
        razao = elem_sequencia[i+1] - elem_sequencia[i]
        lista_de_blocos.append(blocos)
        blocos.clear()
        blocos.append(elem_sequencia[i])
lista_de_blocos.append(blocos)
if (elem_sequencia[N_elem-1] - elem_sequencia[N_elem-2]) == razao:
    blocos.append(elem_sequencia[N_elem-1])
else:
    lista_de_blocos.append(blocos)
    blocos.clear()
    blocos.append(elem_sequencia[N_elem-1])
print(len(lista_de_blocos))