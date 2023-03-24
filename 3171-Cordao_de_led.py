N, L = map(int, input().split())
matrix = [[]] * N
line = [1]
conecteds = [False] * N
avaliator = True

for i in range(len(matrix)):
    matrix[i] = [False] * N

for i in range(L):
    X, Y = map(int, input().split())
    matrix[X - 1][Y - 1] = True
    matrix[Y - 1][X - 1] = True

while len(line) != 0:
    x = line.pop(0)
    if not conecteds[x]:
        conecteds[x] = True
        for i in range(N):
            if matrix[x][i]:
                line.append(i)

for i in conecteds:
    avaliator = avaliator and i

if not avaliator:
    print("INCOMPLETE")
else:
    print("COMPLETE")
