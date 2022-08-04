N = int(input())
secoes = list(map(int, input().split()))
soma=0
somaAcumulada=0
cortes=0
for i in range(N):
    soma+=secoes[i]
while somaAcumulada<(soma/2):
    somaAcumulada+=secoes[cortes]
    cortes+=1
print(cortes)