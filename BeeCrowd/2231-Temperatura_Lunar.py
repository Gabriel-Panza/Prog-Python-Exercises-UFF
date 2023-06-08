n, m = map(int,input().split())
cont = 0
while n != 0 and m != 0:
    cont += 1
    temperature_sequence = [int(input()) for i in range(n)]

    lista_soma = []
    aux = 0
    for i in range(n):
        soma = temperature_sequence[i] + aux
        aux = soma
        lista_soma.append(soma)

    menor = (lista_soma[m-1])/m
    maior = (lista_soma[m-1])/m
    for i in range(m,len(lista_soma),1):
        if (lista_soma[i] - lista_soma[i-m])/m > maior:
                maior = (lista_soma[i] - lista_soma[i-m])/m
        if (lista_soma[i] - lista_soma[i-m])/m < menor:
                menor = (lista_soma[i] - lista_soma[i-m])/m

    print(f"Teste {cont}")
    print(int(menor),int(maior))
    print()
    
    n, m = map(int, input().split())