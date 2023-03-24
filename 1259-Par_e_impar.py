qnt_elements = int(input())
vector = []

for i in range(qnt_elements):
    x = int(input())
    vector.append(x)

vector.sort()
for i in vector:
    if (i % 2) == 0:
        print(i)

for i in range(len(vector)):
    if (vector[len(vector) - i - 1] % 2) != 0:
        print(vector[len(vector) - i - 1])
