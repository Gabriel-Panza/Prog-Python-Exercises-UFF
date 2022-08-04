N_qntd_numeros = int(input())
N_numeros = list(map(int, input().split()))
maiorSequencia=[]
cont=1
for i in range(N_qntd_numeros-1):
    if N_numeros[i]==N_numeros[i+1]:
        cont+=1
    else:
        maiorSequencia.append(cont)
        cont=1
maiorSequencia.append(cont)
maiorSequencia.sort()
print(maiorSequencia[-1])