N = int(input())
cont = 1
V = []
V.append(int(input()))
for i in range(0,N-1):
    V.append(int(input()))
    if V[i+1] != V[i]:
        cont += 1
print(cont)