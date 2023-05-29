N, I, F = input().split()
lista = list(map(int,input().split()))
N = int(N)
I = int(I)
F = int(F)
cont = 0

if ((2 <= N <= 1000) and (-2000 <= I <= 2000) and (-2000 <= F <= 2000)):
    for i in range(0,N):
        for c in range(i+1,N):
            soma = lista[i] + lista[c]
            if I <= soma <= F:
                cont += 1
print(cont)