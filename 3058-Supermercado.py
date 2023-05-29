N = int(input())
menor = float('inf')
for i in range(N):
    P, G = input().split()
    P = float(P)
    G = int(G)
    if (P / G) < menor:
        menor = (P / G)
print("%.2f" % (menor * 1000))