posts , dim = map(int, input().split())
local = list(map(int, input().split()))
cont = 0

for i in range(posts - 1):
    if local[i+1] - local[i] > dim:
        cont += 1
if 42195-local[-1] > dim:
    cont+=1

if cont == 0:
    print('S')
else:
    print('N')