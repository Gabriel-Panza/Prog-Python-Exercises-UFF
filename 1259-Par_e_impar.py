qntd_termos = int(input())
vetor = []

for i in range(qntd_termos):
    x = int(input())
    vetor.append(x)

# for i in range(qntd_termos):
# ----for j in range(qntd_termos):
# --------if vetor[i] < vetor[j]:
# ------------termo_x = vetor[i]
# ------------vetor[i] = vetor[j]
# ------------vetor[j] = termo_x

vetor.sort()
for i in vetor:
    if (i % 2) == 0:
        print(i)

for i in range(len(vetor)):
    if (vetor[len(vetor) - i - 1] % 2) != 0:
        print(vetor[len(vetor) - i - 1])
